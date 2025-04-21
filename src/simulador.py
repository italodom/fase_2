from src.common.utils import get_repositorio

repo = get_repositorio("colheitas")

async def simular_perda_total(hectares_planejados: float, media_perda_por_hectare: float):
    if hectares_planejados < 0 or media_perda_por_hectare < 0:
        print("⚠️ Os valores de hectares e média de perda devem ser positivos.")
        return

    perda_total = hectares_planejados * media_perda_por_hectare
    print("\n📈 Simulação de Perda Total:")
    print(f"Área planejada: {hectares_planejados} ha")
    print(f"Média histórica de perda: {media_perda_por_hectare} t/ha")
    print(f"🔻 Perda estimada: {round(perda_total, 2)} toneladas")

async def calcular_media_perda_por_hectare():
    colheitas = await repo.listar()

    total_perda = 0
    total_hectares = 0

    for c in colheitas:
        hectares = c.get("hectares", None)
        if hectares and "perda_estimada" in c:
            total_perda += c.get("perda_estimada", 0)
            total_hectares += hectares

    if total_hectares == 0:
        print("⚠️ Nenhum dado com hectare registrado.")
        return 0.0

    media = total_perda / total_hectares
    print(f"\n📊 Média histórica de perda: {round(media, 2)} t/ha")
    return media

async def simular_por_turno(turno_desejado: str):
    if not turno_desejado:
        print("⚠️ É necessário informar um turno válido.")
        return

    colheitas = await repo.listar()
    perdas = [c.get("perda_estimada", 0) for c in colheitas
              if c.get("condicoes", {}).get("turno") == turno_desejado
              and "perda_estimada" in c]

    if not perdas:
        print(f"⚠️ Nenhuma colheita registrada no turno '{turno_desejado}'.")
        return

    media = sum(perdas) / len(perdas)
    print(f"\n🕒 Simulação de perda para o turno '{turno_desejado}':")
    print(f"Média estimada de perda: {round(media, 2)} t")