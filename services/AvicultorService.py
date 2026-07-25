from helpers.logger import logger
from repositories.AvicultorRepository import AvicultorRepository
from models.Avicultor import Avicultor


def rowToAvicultor(row):
    id = row[0]
    nome = row[1]
    nascimento = row[2]
    cpf = row[3]
    caf = row[4]
    return Avicultor(id, nome, nascimento, cpf, caf)


class AvicultorService():

    def __init__(self):
        self.avicultorRepository = AvicultorRepository()

    def getAll(self, filtros, dict = None):
        rows = self.avicultorRepository.getAll(filtros)
        logger.info(f"Retornando {len(rows)} avicultores")
        return [rowToAvicultor(r) for r in rows]  

    def getByIdAvicultor(self, id):
        row = self.avicultorRepository.getByIdAvicultor(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return rowToAvicultor(row) if row is not None else None

    def create(self, data):
        nome = data["nome"]
        nascimento = str(data["nascimento"])
        cpf = data["cpf"]
        caf = data["caf"]
        id = self.avicultorRepository.insert(
            nome, nascimento, cpf, caf
        )
        logger.info(f"Avicultor criado com id: {id}")
        return Avicultor(id,  nome, nascimento, cpf, caf)  

    def update(self, id, data):
        affected = self.avicultorRepository.update(
            id, data["nome"], str(data["nascimento"]), data["cpf"], data["caf"]
        )
        if affected == 0:
            return None
        logger.info(f"Avicultor {id} atualizado")
        return Avicultor(id, data["nome"], str(data["nascimento"]), data["cpf"], data["caf"])

    def delete(self, id):
        affected = self.avicultorRepository.delete(id)
        logger.info(f"Avicultor {id} removido: {affected > 0}")
        return affected > 0