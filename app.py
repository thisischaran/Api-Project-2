
from flask_jwt_extended import JWTManager

from flask import Flask, request


app = Flask(__name__)

app = JWTManager(app)

if __name__ =="__main__":
    app.run()


