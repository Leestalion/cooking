from .. import db

class Ingredient(db.Model):
	"""Stores ingredients of a recipe."""
	__tablename__ = 'recipe_ingredient'

	id = db.Column(db.Integer, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))

	ing_name = db.Column(db.String(255))
	quantity = db.Column(db.Integer)
	unity = db.Column(db.Integer)

	# Relationship
	recipe = db.relationship(
		'Recipe',
		backref = db.backref('recipe_ingredient', lazy='dynamic', collection_class=list)
	)