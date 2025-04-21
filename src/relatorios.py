from collections import defaultdict
from statistics import mean

from src.common.utils import get_repositorio

repo = get_repositorio("colheitas")

async def relatorio_por_talhao():
    colheitas = await repo.listar()
    resultado = defaultdict(list)

    for c in colheitas:
        resultado[c["talhao_id"]].append(c["perda_estimada"])

    print("\n📊 Perda Estimada por Talhão:")
    for talhao_id, perdas in resultado.items():
        print(f"Talhão {talhao_id}: média de {round(mean(perdas), 2)} toneladas perdidas")

async def relatorio_por_operador():
    colheitas = await repo.listar()
    operador_stats = defaultdict(lambda: {"total": 0, "perda": 0})

    for c in colheitas:
        stats = operador_stats[c["operador_id"]]
        stats["total"] += c["quantidade_colhida"]
        stats["perda"] += c["perda_estimada"]

    print("\n👷 Desempenho por Operador:")
    for operador_id, stats in operador_stats.items():
        taxa_perda = (stats["perda"] / stats["total"]) * 100 if stats["total"] else 0
        print(f"Operador {operador_id}: {round(stats['total'], 2)} t colhidas — {round(taxa_perda, 2)}% de perda")

async def relatorio_por_maquina():
    colheitas = await repo.listar()
    maquina_stats = defaultdict(lambda: {"total": 0, "perda": 0})

    for c in colheitas:
        stats = maquina_stats[c["maquina_id"]]
        stats["total"] += c["quantidade_colhida"]
        stats["perda"] += c["perda_estimada"]

    print("\n🚜 Desempenho por Máquina:")
    for maq_id, stats in maquina_stats.items():
        taxa = (stats["perda"] / stats["total"]) * 100 if stats["total"] else 0
        print(f"Máquina {maq_id}: {round(stats['total'], 2)} t — {round(taxa, 2)}% de perda")

async def ranking_causas_perda():
    colheitas = await repo.listar()
    causas = defaultdict(int)

    for c in colheitas:
        if c["causa_perda"]:
            causas[c["causa_perda"]] += 1

    print("\n🔎 Causas mais frequentes de perda:")
    for causa, qtd in sorted(causas.items(), key=lambda x: x[1], reverse=True):
        print(f"{causa}: {qtd} ocorrência(s)")

async def resumo_geral():
    colheitas = await repo.listar()
    total_colhido = sum(c["quantidade_colhida"] for c in colheitas)
    total_perda = sum(c["perda_estimada"] for c in colheitas)

    perda_percentual = (total_perda / total_colhido) * 100 if total_colhido else 0

    print("\n📌 RESUMO GERAL:")
    print(f"Total colhido: {round(total_colhido, 2)} t")
    print(f"Total de perda estimada: {round(total_perda, 2)} t")
    print(f"Taxa média de perda: {round(perda_percentual, 2)}%")