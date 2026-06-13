from helpers.logger import logger
from repositories.GalpaoRepository import GalpaoRepository
from models.Galpao import Galpao


def rowToGalpao(row):
    id = row[0]
    identificador = row[1]
    area_m2 = row[2]
    return Galpao(id, identificador, area_m2)

class GalpaoService():
    def __init__(self):
        self.galpaoRepository = GalpaoRepository()

    def getAll(self):
        rows = self.galpaoRepository.getAll()
        logger.info(f"Retornando {len(rows)} galpões")
        return [rowToGalpao(r) for r in rows]

    def getByIdGalpao(self, id):
        row = self.galpaoRepository.getByIdGalpao(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return rowToGalpao(row) if row is not None else None

    def create(self, data):
        identificador = data["identificador"]
        area_m2 = data["area_m2"]
        id = self.galpaoRepository.insert(
            identificador, area_m2
        )
        logger.info(f"Galpão criado com id: {id}")
        return Galpao(id, identificador, area_m2)

    def update(self, id, data):
        affected = self.galpaoRepository.update(
            id, data["identificador"], data["area_m2"]
        )
        if affected == 0:
            return None
        logger.info(f"Galpão {id} atualizado")
        return Galpao(id, data["identificador"], data["area_m2"])

    def delete(self, id):
        affected = self.galpaoRepository.delete(id)
        logger.info(f"Galpão {id} removido: {affected > 0}")
        return affected > 0