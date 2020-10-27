from flask_restful import Resource
from flask import jsonify, request

from src.models.pessoa import Pessoa
from src.utils.parser import parser_pessoa


class PessoasController(Resource):

    @staticmethod
    def get():
        return jsonify(Pessoa.get_pessoa())

    @staticmethod
    def post():
        body = request.json
        return Pessoa.insert_pessoa(body)


class PessoaController(Resource):

    @staticmethod
    def get(id):
        return jsonify(parser_pessoa(Pessoa.get_pessoa_by_id(id)))

    @staticmethod
    def put(id):
        body = request.json
        return Pessoa.update_pessoa(id, body)

    @staticmethod
    def delete(id):
        return Pessoa.delete_pessoa_by_id(id)
