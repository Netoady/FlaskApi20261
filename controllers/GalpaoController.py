from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError

from models.Galpao import GalpaoSchema
from services.GalpaoService import GalpaoService
from helpers.logger import logger

CAMPOS_FILTRO = {"identificador", "area_m2"}

class GalpoesController(Resource):
    def get(self):
        logger.info("Listando todos os galpoes")
        filtros = {key: value for key, value in request.args.items() if key in CAMPOS_FILTRO and value}
        galpoes = GalpaoService().getAll(filtros)
        return [g.toDict() for g in galpoes], 200

    def post(self):
        try:
            data = GalpaoSchema().load(request.get_json())
            galpao = GalpaoService().create(data)
            return galpao.toDict(), 201
        except ValidationError as err:
            return jsonify(err.messages), 400

class GalpaoController(Resource):
    def get(self, galpao_id):
        logger.info(f"Listando galpao pelo id: {galpao_id}")
        galpao = GalpaoService().getByIdGalpao(galpao_id)
        if galpao is None:
            return {"mensagem": "O galpao não foi encontrado"}, 404
        return galpao.toDict(), 200

    

    def put(self, galpao_id):
        try:
            data = GalpaoSchema().load(request.get_json())
            galpao = GalpaoService().update(galpao_id, data)
            if galpao is None:
                return {"mensagem": "O galpao não foi encontrado"}, 404
            return galpao.toDict(), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

        

    def delete(self, galpao_id):
        logger.info(f"Removendo galpao id: {galpao_id}")
        removido = GalpaoService().delete(galpao_id)
        if not removido:
            return {"mensagem": "O galpao não foi encontrado"}, 404
        return {"mensagem": "Galpao removido com sucesso!"}, 200

