from flask_restful import Resource


class HealthController(Resource):

    @staticmethod
    def get():
        return 'Health!'
