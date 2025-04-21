from src.common.utils import gerar_id, get_repositorio

repo = get_repositorio('maquinas')

async def cadastrar_maquina(modelo: str, ano: int, tipo: str):
    maquina = {
        "id": gerar_id(),
        "modelo": modelo,
        "ano": ano,
        "tipo": tipo
    }
    await repo.inserir(maquina)
    print(f"Máquina '{modelo}' cadastrada com sucesso! ID: {maquina['id']}")

async def listar_maquinas():
    maquinas = await repo.listar()
    if not maquinas:
        print("Nenhuma máquina cadastrada.")
        return

    print("Lista de Máquinas:")
    for maquina in maquinas:
        print(f"ID: {maquina['id']}")
        print(f"Modelo: {maquina['modelo']}")
        print(f"Ano: {maquina['ano']}")
        print(f"Tipo: {maquina['tipo']}")
        print("-" * 30)

async def atualizar_maquina(id_maquina: str, modelo: str, ano: int, tipo: str):
    novos_dados = {
        "modelo": modelo,
        "ano": ano,
        "tipo": tipo
    }
    resultado = await repo.atualizar(id_maquina, novos_dados)

    if resultado:
        print(f"Máquina com ID '{id_maquina}' atualizada com sucesso!")
    else:
        print(f"Erro: Máquina com ID '{id_maquina}' não encontrada.")

async def deletar_maquina(id_maquina: str):
    resultado = await repo.deletar(id_maquina)
    if resultado:
        print(f"Máquina com ID '{id_maquina}' removida com sucesso!")
    else:
        print(f"Erro: Máquina com ID '{id_maquina}' não encontrada.")