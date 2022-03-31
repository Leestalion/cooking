from .. import db

class RecipeIngredient(db.Model):
	"""Stores ingredients of a recipe."""
	__tablename__ = 'recipe_ingredient'

	recipe_ingredient_id = db.Column(db.Integer, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'))
	ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.ingredient_id'))
	quantity = db.Column(db.Integer)
	unity = db.Column(db.Integer)

	def __init__(self, recipe_id, ingredient_id, quantity, unity) -> None:
		super().__init__()
		self.recipe_id = recipe_id
		self.ingredient_id = ingredient_id
		self.quantity = quantity
		self.unity = unity

	
	@staticmethod
	def create(recipe_id, ingredient_id, quantity, unity):
		ingredient = RecipeIngredient(
			recipe_id = recipe_id,
			ingredient_id = ingredient_id,
			quantity = quantity,
			unity = unity,
		)
		db.session.add(ingredient)
		db.session.commit()
		return ingredient

	@staticmethod
	def deleteByRecipeId(recipe_id):
		for recipeIngredient in RecipeIngredient.query.filter_by(recipe_id=recipe_id).all():
			db.session.delete(recipeIngredient)
		
		db.session.commit()

	# Relationship
	recipe = db.relationship(
		'Recipe',
		backref = db.backref('recipe_ingredient', lazy='dynamic', collection_class=list)
	)
	ingredient = db.relationship(
		'Ingredient',
		backref = db.backref('recipe_ingredient', lazy='dynamic', collection_class=list)
	)