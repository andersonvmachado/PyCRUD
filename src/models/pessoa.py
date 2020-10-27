from src.models import db

from src.utils.parser import parser_pessoa

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    salario = db.Column(db.Float)
    dt_nascimento = db.Column(db.Date)

    @staticmethod
    def get_pessoa():
        pessoas = Pessoa.query.all()
        return [parser_pessoa(pessoa) for pessoa in pessoas]

    @staticmethod
    def get_pessoa_by_id(id):
        return Pessoa.query.filter_by(id=id).first()

    @staticmethod
    def delete_pessoa_by_id(id):
        try:
            Pessoa.query.filter_by(id=id).delete()
            db.session.commit()
            return True
        except Exception as e:
            print('Error on delete pessoa', str(e))
            return False

    @staticmethod
    def insert_pessoa(pessoa):
        new_pessoa = Pessoa()
        new_pessoa.nome = pessoa['nome']
        new_pessoa.email = pessoa['email']
        new_pessoa.salario = pessoa['salario']
        new_pessoa.dt_nascimento = pessoa['dt_nascimento']

        db.session.add(new_pessoa)
        db.session.commit()

        return parser_pessoa(new_pessoa)

    @staticmethod
    def update_pessoa(id, pessoa):
        alt_pessoa = Pessoa.get_pessoa_by_id(id)

        alt_pessoa.nome = pessoa['nome']
        alt_pessoa.email = pessoa['email']
        alt_pessoa.salario = pessoa['salario']
        alt_pessoa.dt_nascimento = pessoa['dt_nascimento']

        #db.session.update(alt_pessoa)
        db.session.commit()

        return parser_pessoa(alt_pessoa)