from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.settings import URI_CONNECTION, PORT
from src.routes import init_resources


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = URI_CONNECTION
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
init_resources(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
