from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from ..models.recipe import Recipe

from ..models.ingredient import Ingredient
from ..models.user import User

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
    
    user_id = auto_field()
    name = auto_field()
    email = auto_field()
    profile_pic = auto_field()


class IngredientSchema(SQLAlchemySchema):
    class Meta:
        model = Ingredient
    
    ingredient_id = auto_field()
    ingredient_name = auto_field()
    unity = auto_field()

class RecipeSchema(SQLAlchemySchema):

    class Meta:
        model = Recipe
    
    recipe_id = auto_field()
    name = auto_field()
    time = auto_field()
    difficulty = auto_field()
    user_id = auto_field()

user_schema = UserSchema()
ingredients_schema = IngredientSchema(many = True)
ingredient_schema = IngredientSchema()
recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many = True)