from flask import request, jsonify
from flask_restful import Resource
from marshmallow import ValidationError

from models.Avicula import AviculaSchema
from services.AviculaService import AviculaService
from helpers.logger import logger

CAMPOS_FILTRO = {"name", "cnpj", "endereco"}

class AviculasController(Resource):
    def get(self):
        logger.info("Listando todos os aviculas")
        filtros = {key: value for key, value in request.args.items() if key in CAMPOS_FILTRO and value}
        aviculas = AviculaService().getAll(filtros)
        return [a.toDict() for a in aviculas], 200

    def post(self):
        try:
            data = AviculaSchema().load(request.get_json())
            avicula = AviculaService().create(data)
            return avicula.toDict(), 201
        except ValidationError as err:
            return jsonify(err.messages), 400

class AviculaController(Resource):
    def get(self, avicula_id):
        logger.info(f"Listando avicula pelo id: {avicula_id}")
        avicula = AviculaService().getByIdAvicula(avicula_id)
        if avicula is None:
            return {"mensagem": "O avicula não foi encontrado"}, 404
        return avicula.toDict(), 200

    def put(self, avicula_id):
        try:
            data = AviculaSchema().load(request.get_json())
            avicula = AviculaService().update(avicula_id, data)
            if avicula is None:
                return {"mensagem": "O avicula não foi encontrado"}, 404
            return avicula.toDict(), 200
        except ValidationError as err:
            return jsonify(err.messages), 400

    def delete(self, avicula_id):
        logger.info(f"Removendo avicula id: {avicula_id}")
        removido = AviculaService().delete(avicula_id)
        if not removido:
            return {"mensagem": "O avicula não foi encontrado"}, 404
        return {"mensagem": "Avicula removido com sucesso!"}, 200