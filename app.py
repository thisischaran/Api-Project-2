
from flask_jwt_extended import JWTManager

from flask import Flask, request

from db import db


app = Flask("__name__")

jwt = JWTManager(app)


if __name__ == "__main__":
    app.run()


