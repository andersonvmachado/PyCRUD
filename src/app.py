from os import getenv
from flask import Flask

from src.controllers.user import get_user

app = Flask(__name__)

DB_HOST = getenv('DB_HOST')


@app.route("/user")
def user():
    return get_user()

if __name__ == "__main__":
    app.run()
