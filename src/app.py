from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.settings import URI_CONNECTION
from src.routes import init_resources


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = URI_CONNECTION
db = SQLAlchemy(app)
init_resources(app)

if __name__ == "__main__":
    app.run()
