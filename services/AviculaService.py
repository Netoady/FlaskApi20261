from helpers.logger import logger
from repositories.AviculaRepository import AviculaRepository
from models.Avicula import Avicula


def rowToAvicula(row):
    id = row[0]
    nome = row[1]
    cnpj = row[2]
    endereco = row[3]
    return Avicula(id, nome, cnpj, endereco)

class AviculaService():
    def __init__(self):
        self.aviculaRepository = AviculaRepository()

    def getAll(self):
        rows = self.aviculaRepository.getAll()
        logger.info(f"Retornando {len(rows)} aviculas")
        return [rowToAvicula(r) for r in rows]

    def getByIdAvicula(self, id):
        row = self.aviculaRepository.getByIdAvicula(id)
        logger.info("Lendo informações do resultado da consulta ao banco")
        return rowToAvicula(row) if row is not None else None

    def create(self, data):
        nome = data["nome"]
        cnpj = str(data["cnpj"])
        endereco = data["endereco"]
        id = self.aviculaRepository.insert(
            nome, cnpj, endereco
        )
        logger.info(f"Avicula criado com id: {id}")
        return Avicula(id,  nome, cnpj, endereco)

    def update(self, id, data):
        affected = self.aviculaRepository.update(
            id, data["nome"], str(data["cnpj"]), data["endereco"]
        )
        if affected == 0:
            return None
        logger.info(f"Avicula {id} atualizada")
        return Avicula(id, data["nome"], str(data["cnpj"]), data["endereco"])

    def delete(self, id):
        affected = self.aviculaRepository.delete(id)
        logger.info(f"Avicula {id} removida: {affected > 0}")
        return affected > 0