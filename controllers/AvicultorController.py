from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError

from models.Avicultor import AvicultorSchema
from services.AvicultorService import AvicultorService
from helpers.logger import logger

CAMPOS_FILTRO = {"nome", "cpf", "caf"}

class AvicultoresController(Resource):
    def get(self):
        logger.info("Listando todos os avicultores")
        filtros = {key: value for key, value in request.args.items() if key in CAMPOS_FILTRO and value}
        avicultores = AvicultorService().getAll(filtros)
        return [a.toDict() for a in avicultores], 200

    def post(self):
        try:
            data = AvicultorSchema().load(request.get_json())
            avicultor = AvicultorService().create(data)
            return avicultor.toDict(), 201
        except ValidationError as err:
            return jsonify(err.messages), 400

class AvicultorController(Resource):
    def get(self, avicultor_id):
        logger.info(f"Listando avicultor pelo id: {avicultor_id}")
        avicultor = AvicultorService().getByIdAvicultor(avicultor_id)
        if avicultor is None:
            return {"mensagem": "O avicultor não foi encontrado"}, 404
        return avicultor.toDict(), 200



    def put(self, avicultor_id):
        try:
            data = AvicultorSchema().load(request.get_json())
            avicultor = AvicultorService().update(avicultor_id, data)
            if avicultor is None:
                return {"mensagem": "O avicultor não foi encontrado"}, 404
            return avicultor.toDict(), 200
        except ValidationError as err:
            return jsonify(err.messages), 400



    def delete(self, avicultor_id):
        logger.info(f"Removendo avicultor id: {avicultor_id}")
        removido = AvicultorService().delete(avicultor_id)
        if not removido:
            return {"mensagem": "O avicultor não foi encontrado"}, 404
        return {"mensagem": "Avicultor removido com sucesso!"}, 200





