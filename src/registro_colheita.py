from src.common.utils import gerar_id, get_repositorio

repo = get_repositorio('colheitas')

def calcular_perda_estimada(tipo_colheita: str, quantidade: float) -> float:
    if tipo_colheita.lower() == "manual":
        return round(quantidade * 0.05, 2)
    elif tipo_colheita.lower() == "mecanica":
        return round(quantidade * 0.15, 2)
    else:
        return 0.0

async def selecionar_talhao():
    repo_talhoes = get_repositorio('talhoes')
    talhoes = await repo_talhoes.listar()

    if not talhoes or len(talhoes) == 0:
        print("Não há talhões cadastrados. Por favor, cadastre um talhão primeiro.")
        return None

    print("\n--- Selecione um Talhão ---")
    for i, talhao in enumerate(talhoes, 1):
        print(f"{i}. {talhao['nome']} - {talhao['localizacao']} ({talhao['hectares']} ha)")

    while True:
        try:
            escolha = int(input("\nDigite o número do talhão: ")) - 1
            if 0 <= escolha < len(talhoes):
                return talhoes[escolha]['id']
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número.")

async def selecionar_operador():
    repo_operadores = get_repositorio('operadores')
    operadores = await repo_operadores.listar()

    if not operadores or len(operadores) == 0:
        print("Não há operadores cadastrados. Por favor, cadastre um operador primeiro.")
        return None

    print("\n--- Selecione um Operador ---")
    for i, operador in enumerate(operadores, 1):
        print(f"{i}. {operador['nome']} - Turno: {operador['turno']}")

    while True:
        try:
            escolha = int(input("\nDigite o número do operador: ")) - 1
            if 0 <= escolha < len(operadores):
                return operadores[escolha]['id']
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número.")

async def selecionar_maquina():
    repo_maquinas = get_repositorio('maquinas')
    maquinas = await repo_maquinas.listar()

    if not maquinas or len(maquinas) == 0:
        print("Não há máquinas cadastradas. Por favor, cadastre uma máquina primeiro.")
        return None

    print("\n--- Selecione uma Máquina ---")
    for i, maquina in enumerate(maquinas, 1):
        print(f"{i}. {maquina['modelo']} ({maquina['ano']}) - Tipo: {maquina['tipo']}")

    while True:
        try:
            escolha = int(input("\nDigite o número da máquina: ")) - 1
            if 0 <= escolha < len(maquinas):
                return maquinas[escolha]['id']
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número.")

async def registrar_colheita(
        talhao_id: str,
        operador_id: str,
        maquina_id: str,
        tipo_colheita: str,
        quantidade_colhida: float,
        perda_real: float = None,
        causa_perda: str = "",
        severidade: str = "",
        condicoes: dict = None,
        data: str = None
):
    colheita = {
        "id": gerar_id(),
        "talhao_id": talhao_id,
        "operador_id": operador_id,
        "maquina_id": maquina_id,
        "tipo_colheita": tipo_colheita,
        "quantidade_colhida": quantidade_colhida,
        "perda_estimada": calcular_perda_estimada(tipo_colheita, quantidade_colhida),
        "perda_real": perda_real,
        "causa_perda": causa_perda,
        "severidade": severidade,
        "condicoes": condicoes or {},
        "data": data
    }

    await repo.inserir(colheita)
    print(f"Colheita registrada com sucesso! ID: {colheita['id']}")
    return colheita

async def listar_colheitas():
    colheitas = await repo.listar()
    if not colheitas:
        print("Não há colheitas registradas.")
    else:
        print("\n--- Lista de Colheitas ---")
        for colheita in colheitas:
            print(f"ID: {colheita['id']}")
            print(f"Talhão: {colheita['talhao_id']}")
            print(f"Operador: {colheita['operador_id']}")
            print(f"Máquina: {colheita['maquina_id']}")
            print(f"Quantidade: {colheita['quantidade_colhida']} t")
            print(f"Perda Estimada: {colheita['perda_estimada']} t")
            print(f"Perda Real: {colheita['perda_real']} t")
            print(f"Data: {colheita['data']}")
            print("-----------------------")
    return colheitas

async def atualizar_colheita(id_colheita: str, novos_dados: dict):
    resultado = await repo.atualizar(id_colheita, novos_dados)
    if resultado:
        print(f"Colheita {id_colheita} atualizada com sucesso!")
    else:
        print(f"Não foi possível atualizar a colheita {id_colheita}.")
    return resultado

async def deletar_colheita(id_colheita: str):
    resultado = await repo.deletar(id_colheita)
    if resultado:
        print(f"Colheita {id_colheita} deletada com sucesso!")
    else:
        print(f"Não foi possível deletar a colheita {id_colheita}.")
    return resultado