from marshmallow import Schema, fields


class userregisterschema(Schema):
    userid = fields.String(required=True)
    password = fields.String(required=True)

class userregisterresponseschema(Schema):
    msg = fields.String(dump_only=True)

class userloginschema(Schema):
    userid =fields.String(required=True)
    password = fields.String(required=True)

class userloginresponseschema(Schema):
    jwttoken = fields.String(dump_only=True)

class operationschema(Schema):
    number1= fields.Float(required=True)
    number2= fields.Float(required=True)
    
class operationresponseschema(Schema):
    result = fields.Float(dump_only=True)
    
