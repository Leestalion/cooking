from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from ..models.user import User

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
    
    user_id = auto_field()
    name = auto_field()
    email = auto_field()
    profile_pic = auto_field()

user_schema = UserSchema()