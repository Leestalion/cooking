from .. import db


class Step(db.Model):
	"""Stores steps of a recipe."""
	__tablename__ = 'recipe_step'

	id = db.Column(db.Integer, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))

	step_text = db.Column(db.Text())

	# Relationship
	recipe = db.relationship(
		'Recipe',
		backref = db.backref('recipe_step', lazy='dynamic', collection_class=list)
	)