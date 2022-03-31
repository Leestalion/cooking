from .. import db


class Step(db.Model):
	"""Stores steps of a recipe."""
	__tablename__ = 'recipe_step'

	id = db.Column(db.Integer, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))

	step_text = db.Column(db.Text())


	def __init__(self, recipe_id, step_text) -> None:
		super().__init__()
		self.recipe_id = recipe_id
		self.step_text = step_text

	
	@staticmethod
	def create(recipe_id, step_text):
		step = Step(
			recipe_id = recipe_id,
			step_text = step_text,
		)
		db.session.add(step)
		db.session.commit()
		return step

	@staticmethod
	def deleteByRecipeId(recipe_id):
		for step in Step.query.filter_by(recipe_id=recipe_id).all():
			db.session.delete(step)
		
		db.session.commit()

	# Relationship
	recipe = db.relationship(
		'Recipe',
		backref = db.backref('recipe_step', lazy='dynamic', collection_class=list)
	)