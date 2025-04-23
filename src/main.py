import asyncio

from src.maquinas import cadastrar_maquina, listar_maquinas, atualizar_maquina, deletar_maquina
from src.operadores import cadastrar_operador, listar_operadores, atualizar_operador, deletar_operador
from src.registro_colheita import registrar_colheita, listar_colheitas, atualizar_colheita, deletar_colheita, \
    selecionar_talhao, selecionar_operador, selecionar_maquina
from src.relatorios import resumo_geral, relatorio_por_talhao, relatorio_por_operador, relatorio_por_maquina, \
    ranking_causas_perda
from src.talhoes import cadastrar_talhao, listar_talhoes, atualizar_talhao, deletar_talhao


async def menu_principal():
    while True:
        print("""
========= CanaTrack360 =========
1. Talhões
2. Operadores
3. Máquinas
4. Colheitas
5. Relatórios
0. Sair
===============================""")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            await menu_talhoes()
        elif escolha == "2":
            await menu_operadores()
        elif escolha == "3":
            await menu_maquinas()
        elif escolha == "4":
            await menu_colheitas()
        elif escolha == "5":
            await menu_relatorios()
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")

# TALHÕES
async def menu_talhoes():
    while True:
        print("""
--- TALHÕES ---
1. Cadastrar
2. Listar
3. Atualizar
4. Deletar
0. Voltar""")
        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            localizacao = input("Localização: ")
            hectares = float(input("Hectares: "))
            tipo_solo = input("Tipo de solo: ")
            await cadastrar_talhao(nome, localizacao, hectares, tipo_solo)
        elif op == "2":
            await listar_talhoes()  # Removido o 'return' daqui
        elif op == "3":
            id_ = input("ID do talhão: ")
            nome = input("Novo nome: ")
            localizacao = input("Nova localização: ")
            hectares = float(input("Novo hectares: "))
            tipo_solo = input("Novo tipo de solo: ")
            await atualizar_talhao(id_, nome, localizacao, hectares, tipo_solo)
        elif op == "4":
            id_ = input("ID a deletar: ")
            await deletar_talhao(id_)
        elif op == "0":
            break

# OPERADORES
async def menu_operadores():
    while True:
        print("""
--- OPERADORES ---
1. Cadastrar
2. Listar
3. Atualizar
4. Deletar
0. Voltar""")
        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            turno = input("Turno (diurno/noturno): ")
            await cadastrar_operador(nome, turno)
        elif op == "2":
            await listar_operadores()
        elif op == "3":
            id_ = input("ID do operador: ")
            nome = input("Novo nome: ")
            turno = input("Novo turno: ")
            await atualizar_operador(id_, nome, turno)
        elif op == "4":
            id_ = input("ID a deletar: ")
            await deletar_operador(id_)
        elif op == "0":
            break

# MÁQUINAS
async def menu_maquinas():
    while True:
        print("""
--- MÁQUINAS ---
1. Cadastrar
2. Listar
3. Atualizar
4. Deletar
0. Voltar""")
        op = input("Escolha: ")

        if op == "1":
            modelo = input("Modelo: ")
            ano = int(input("Ano: "))
            tipo = input("Tipo: ")
            await cadastrar_maquina(modelo, ano, tipo)
        elif op == "2":
            await listar_maquinas()
        elif op == "3":
            id_ = input("ID da máquina: ")
            modelo = input("Novo modelo: ")
            ano = int(input("Novo ano: "))
            tipo = input("Novo tipo: ")
            await atualizar_maquina(id_, modelo, ano, tipo)
        elif op == "4":
            id_ = input("ID a deletar: ")
            await deletar_maquina(id_)
        elif op == "0":
            break

# COLHEITAS
async def menu_colheitas():
    while True:
        print("""
--- COLHEITAS ---
1. Registrar
2. Listar
3. Atualizar
4. Deletar
0. Voltar""")
        op = input("Escolha: ")

        if op == "1":
            talhao_id = await selecionar_talhao()
            if not talhao_id:
                continue

            operador_id = await selecionar_operador()
            if not operador_id:
                continue

            maquina_id = await selecionar_maquina()
            if not maquina_id:
                continue

            tipo = input("Tipo (manual/mecanica): ")
            qtd = float(input("Qtd colhida (t): "))
            perda = float(input("Perda real (t): "))
            causa = input("Causa da perda: ")
            severidade = input("Severidade (leve/moderada/crítica): ")
            turno = input("Turno: ")
            clima = input("Clima: ")
            solo = input("Solo: ")
            data = input("Data (dd/mm/yyyy): ")

            await registrar_colheita(
                talhao_id, operador_id, maquina_id, tipo, qtd, perda,
                causa, severidade,
                condicoes={"turno": turno, "clima": clima, "solo": solo},
                data=data
            )
        elif op == "2":
            await listar_colheitas()
        elif op == "3":
            id_ = input("ID da colheita: ")
            campo = input("Campo a atualizar (ex: perda_real): ")
            valor = input("Novo valor: ")
            try:
                valor = float(valor) if "." in valor else int(valor)
            except:
                pass
            await atualizar_colheita(id_, {campo: valor})
        elif op == "4":
            id_ = input("ID a deletar: ")
            await deletar_colheita(id_)
        elif op == "0":
            break

# RELATÓRIOS
async def menu_relatorios():
    await resumo_geral()
    await relatorio_por_talhao()
    await relatorio_por_operador()
    await relatorio_por_maquina()
    await ranking_causas_perda()

async def main():
    await menu_principal()

# INÍCIO
if __name__ == "__main__":
    asyncio.run(main())
