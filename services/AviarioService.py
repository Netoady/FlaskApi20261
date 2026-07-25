from helpers.logger import logger
from repositories.AviarioRepository import AviarioRepository
from models.Aviario import Aviario


def rowToAviario(row):
    id = row[0]
    nome = row[1]
    capacidade = row[2]
    return Aviario(id, nome, capacidade)

class AviarioService():
    def __init__(self):
        self.aviarioRepository = AviarioRepository()

    def getAll(self, filtros, dict = None):
        rows = self.aviarioRepository.getAll(filtros)
        logger.info(f"Retornando {len(rows)} aviários")
        return [rowToAviario(r) for r in rows]

    def getByIdAviario(self, id):
        row = self.aviarioRepository.getByIdAviario(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return rowToAviario(row) if row is not None else None

    def create(self, data):
        nome = data["nome"]
        capacidade = data["capacidade"]
        id = self.aviarioRepository.insert(
            nome, capacidade
        )
        logger.info(f"Aviário criado com id: {id}")
        return Aviario(id, nome, capacidade)

    def update(self, id, data):
        affected = self.aviarioRepository.update(
            id, data["nome"], data["capacidade"]
        )
        if affected == 0:
            return None
        logger.info(f"Aviário {id} atualizado")
        return Aviario(id, data["nome"], data["capacidade"])

    def delete(self, id):
        affected = self.aviarioRepository.delete(id)
        logger.info(f"Aviário {id} removido: {affected > 0}")
        return affected > 0