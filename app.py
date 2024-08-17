
from flask_jwt_extended import JWTManager
from flask import Flask
from flask_smorest import Api
from db import db
import models
from resources.users import blp as userblp



app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "rest api with sqlalchemy"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mysite.db"
app.config["JWT_SECRET_KEY"] = "charan"

jwt = JWTManager(app)

db.init_app(app)
api = Api(app)
with app.app_context():
    db.create_all()




api.register_blueprint(userblp)

if __name__ == "__main__":

  
    app.run(debug=True)


