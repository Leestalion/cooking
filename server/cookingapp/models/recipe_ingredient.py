from .. import db

class RecipeIngredient(db.Model):
	"""Stores ingredients of a recipe."""
	__tablename__ = 'recipe_ingredient'

	recipe_ingredient_id = db.Column(db.Integer, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))
	ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.ingredient_id'))
	quantity = db.Column(db.Integer)

	# Relationship
	recipe = db.relationship(
		'Recipe',
		backref = db.backref('recipe_ingredient', lazy='dynamic', collection_class=list)
	)
	ingredient = db.relationship(
		'Ingredient',
		backref = db.backref('recipe_ingredient', lazy='dynamic', collection_class=list)
	)