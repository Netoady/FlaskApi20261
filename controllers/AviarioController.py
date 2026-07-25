from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError

from models.Aviario import AviarioSchema
from services.AviarioService import AviarioService
from helpers.logger import logger

CAMPOS_FILTRO = {"name", "capacidade"}

class AviariosController(Resource):
    def get(self):
        logger.info("Listando todos os aviarios")
        filtros = {key: value for key, value in request.args.items() if key in CAMPOS_FILTRO and value}
        aviarios = AviarioService().getAll(filtros)
        return [a.toDict() for a in aviarios], 200

    def post(self):
        try:
            data = AviarioSchema().load(request.get_json())
            aviario = AviarioService().create(data)
            return aviario.toDict(), 201
        except ValidationError as err:
            return jsonify(err.messages), 400

class AviarioController(Resource):
    def get(self, aviario_id):
        logger.info(f"Listando aviario pelo id: {aviario_id}")
        aviario = AviarioService().getByIdAviario(aviario_id)
        if aviario is None:
            return {"mensagem": "O aviario não foi encontrado"}, 404
        return aviario.toDict(), 200

    def put(self, aviario_id):
        try:
            data = AviarioSchema().load(request.get_json())
            aviario = AviarioService().update(aviario_id, data)
            if aviario is None:
                return {"mensagem": "O aviario não foi encontrado"}, 404
            return aviario.toDict(), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, aviario_id):
        logger.info(f"Removendo aviario id: {aviario_id}")
        removido = AviarioService().delete(aviario_id)
        if not removido:
            return {"mensagem": "O aviario não foi encontrado"}, 404
        return {"mensagem": "Aviario removido com sucesso!"}, 200

