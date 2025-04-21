import uuid
from src.persistencia.adapters.in_memory_repository import InMemoryRepository

_REPOSITORIOS = {
    "talhoes": InMemoryRepository(),
    "maquinas": InMemoryRepository(),
    "operadores": InMemoryRepository(),
    "colheitas": InMemoryRepository()
}

def get_repositorio(nome: str):
    repo = _REPOSITORIOS.get(nome)
    if not repo:
        raise Exception(f"Repositório '{nome}' não encontrado.")
    return repo

def gerar_id():
    return str(uuid.uuid4())