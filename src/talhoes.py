from src.common.utils import gerar_id, get_repositorio

repo = get_repositorio('talhoes')

async def cadastrar_talhao(nome, localizacao, hectares, tipo_solo):
    talhao = {
        "id": gerar_id(),
        "nome": nome,
        "localizacao": localizacao,
        "hectares": hectares,
        "tipo_solo": tipo_solo
    }
    await repo.inserir(talhao)
    print(f"Talhão '{nome}' cadastrado com sucesso! ID: {talhao['id']}")

async def listar_talhoes():
    talhoes = await repo.listar()
    if not talhoes:
        print("Nenhum talhão cadastrado.")
        return

    print("Lista de Talhões:")
    for talhao in talhoes:
        print(f"ID: {talhao['id']}")
        print(f"Nome: {talhao['nome']}")
        print(f"Localização: {talhao['localizacao']}")
        print(f"Hectares: {talhao['hectares']}")
        print(f"Tipo de Solo: {talhao['tipo_solo']}")
        print("-" * 30)

async def atualizar_talhao(id_talhao, nome, localizacao, hectares, tipo_solo):
    resultado = await repo.atualizar(id_talhao, {
        "nome": nome,
        "localizacao": localizacao,
        "hectares": hectares,
        "tipo_solo": tipo_solo
    })

    if resultado:
        print(f"Talhão com ID '{id_talhao}' atualizado com sucesso!")
    else:
        print(f"Erro: Talhão com ID '{id_talhao}' não encontrado.")

async def deletar_talhao(id_talhao):
    resultado = await repo.deletar(id_talhao)
    if resultado:
        print(f"Talhão com ID '{id_talhao}' removido com sucesso!")
    else:
        print(f"Erro: Talhão com ID '{id_talhao}' não encontrado.")