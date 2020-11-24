from main import ma
from models.User import User 
from marshmallow.validate import Length, Email


# Validate user info before going into the database
# we should validate info from the user before we try to insert it into the database
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
    email = ma.String(required=True, validate=[Length(min=4), Email()])
    password = ma.String(required=True, validate=Length(min=6))



user_schema = UserSchema()
users_schema = UserSchema(many=True)