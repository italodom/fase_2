import uuid

from src.persistencia.adapters.oracle_repository import OracleRepository

CONNECTION_STRING = "dev/dev123@localhost:1521/freepdb1"

_REPOSITORIOS = {
    "talhoes": OracleRepository(CONNECTION_STRING, "talhoes"),
    "maquinas": OracleRepository(CONNECTION_STRING, "maquinas"),
    "operadores": OracleRepository(CONNECTION_STRING, "operadores"),
    "colheitas": OracleRepository(CONNECTION_STRING, "colheitas")
}

def get_repositorio(nome: str):
    repo = _REPOSITORIOS.get(nome)
    if not repo:
        raise Exception(f"Repositório '{nome}' não encontrado.")
    return repo

def gerar_id():
    return str(uuid.uuid4())