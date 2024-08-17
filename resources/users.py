from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask_jwt_extended import create_access_token, jwt_required
from models import dbusertable, dblogouttable
from db import db
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


from Schema import userloginschema, userloginresponseschema, userregisterschema, userregisterresponseschema


blp = Blueprint("users",__name__,description ="useer operations")

@blp.route('/register')
class userlogin(MethodView):
    @blp.arguments(userloginschema)
    @blp.response(201,userloginresponseschema)
    def post(self,user_data):
        reguser = dbusertable(**user_data)
        try:

            db.session.add(reguser)
            db.session.commit()

        except IntegrityError:
            abort(400, message="user id already available")
        except SQLAlchemyError:
             abort(400, message="some database error ")

        
              

        return {"jwttoken":"wait fot token"}

    