import json
from flask_restful import Resource
from flask import jsonify, request

from src.models.pessoa import Pessoa
from src.utils.parser import parser_pessoa
from src.controllers import redis_client


class PessoasController(Resource):

    @staticmethod
    def get():
        cache = redis_client.hget(name="allpeoples", key="peoples-qry")
        if cache:
            return jsonify(json.loads(cache))

        data = Pessoa.get_pessoa()

        redis_client.hset(
            name="allpeoples",
            key="peoples-qry",
            value=json.dumps(data)
        )

        return jsonify(data)

    @staticmethod
    def post():
        body = request.json
        redis_client.hdel("allpeoples", "peoples-qry")
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
