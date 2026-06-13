from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from models.Avicultor import AvicultorSchema
from services.AvicultorService import AvicultorService
from helpers.logger import logger

avicultor_bp = Blueprint('avicultor', __name__, url_prefix='/avicultores')


@avicultor_bp.get("/")
def getAvicultores():
    logger.info("Listando todos os avicultores")
    avicultores = AvicultorService().getAll()
    return [a.toDict() for a in avicultores], 200


@avicultor_bp.get("/<int:id>")
def getByIdAvicultores(id: int):
    logger.info(f"Listando avicultor pelo id: {id}")
    avicultor = AvicultorService().getByIdAvicultor(id)
    if avicultor is None:
        return {"mensagem": "O avicultor não foi encontrado"}, 404
    return avicultor.toDict(), 200


@avicultor_bp.post("/")
def postAvicultores():
    try:
        data = AvicultorSchema().load(request.get_json())
        avicultor = AvicultorService().create(data)
        return avicultor.toDict(), 201
    except ValidationError as err:
        return jsonify(err.messages), 400


@avicultor_bp.put("/<int:id>")
def putAvicultores(id: int):
    try:
        data = AvicultorSchema().load(request.get_json())
        avicultor = AvicultorService().update(id, data)
        if avicultor is None:
            return {"mensagem": "O avicultor não foi encontrado"}, 404
        return avicultor.toDict(), 200
    except ValidationError as err:
        return jsonify(err.messages), 400


@avicultor_bp.delete("/<int:id>")
def deleteAvicultores(id: int):
    logger.info(f"Removendo avicultor id: {id}")
    removido = AvicultorService().delete(id)
    if not removido:
        return {"mensagem": "O avicultor não foi encontrado"}, 404
    return {"mensagem": "Avicultor removido com sucesso!"}, 200