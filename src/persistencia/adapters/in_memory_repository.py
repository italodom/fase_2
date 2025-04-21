from src.persistencia.base_repository import BaseRepository


class InMemoryRepository(BaseRepository):
    def __init__(self):
        self._dados = []

    async def inserir(self, entidade):
        self._dados.append(entidade)

    async def listar(self):
        return self._dados

    async def atualizar(self, id, novos_dados):
        for item in self._dados:
            if item["id"] == id:
                item.update(novos_dados)
                return True
        return False

    async def deletar(self, id):
        for i, item in enumerate(self._dados):
            if item["id"] == id:
                del self._dados[i]
                return True
        return False