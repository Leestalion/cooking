from .. import db

class Ingredient(db.Model):
	"""Stores ingredients."""
	__tablename__ = 'ingredient'

	ingredient_id = db.Column(db.Integer, primary_key=True)
	ingredient_name = db.Column(db.String(255))
	unity = db.Column(db.Integer)