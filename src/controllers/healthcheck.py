from flask_restful import Resource
from src.controllers import redis_client


class HealthController(Resource):

    @staticmethod
    def get():
        result = redis_client.ping()
        return f'Health - {result}!'
