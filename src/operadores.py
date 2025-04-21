from src.common.utils import gerar_id, get_repositorio

repo = get_repositorio('operadores')

async def cadastrar_operador(nome: str, turno: str):
    operador = {
        "id": gerar_id(),
        "nome": nome,
        "turno": turno
    }
    await repo.inserir(operador)
    print(f"Operador '{nome}' cadastrado com sucesso! ID: {operador['id']}")

async def listar_operadores():
    operadores = await repo.listar()
    if not operadores:
        print("Nenhum operador cadastrado.")
        return

    print("Lista de Operadores:")
    for operador in operadores:
        print(f"ID: {operador['id']}")
        print(f"Nome: {operador['nome']}")
        print(f"Turno: {operador['turno']}")
        print("-" * 30)

async def atualizar_operador(id_operador: str, nome: str, turno: str):
    novos_dados = {
        "nome": nome,
        "turno": turno
    }
    resultado = await repo.atualizar(id_operador, novos_dados)

    if resultado:
        print(f"Operador com ID '{id_operador}' atualizado com sucesso!")
    else:
        print(f"Erro: Operador com ID '{id_operador}' não encontrado.")

async def deletar_operador(id_operador: str):
    resultado = await repo.deletar(id_operador)
    if resultado:
        print(f"Operador com ID '{id_operador}' removido com sucesso!")
    else:
        print(f"Erro: Operador com ID '{id_operador}' não encontrado.")