from flask_restful import Api

from src.controllers.healthcheck import HealthController
from src.controllers.pessoa import PessoaController, PessoasController


def init_resources(app):
    api = Api()

    api.add_resource(HealthController, "/health-check")
    api.add_resource(PessoasController, "/pessoas")
    api.add_resource(PessoaController, "/pessoas/<int:id>")


    api.init_app(app)


