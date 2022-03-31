from .. import db

class Recipe(db.Model):
	"""Stores recipes."""
	__tablename__ = 'recipe'

	recipe_id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer(), db.ForeignKey('user.user_id'))
	time = db.Column(db.String(255))
	name = db.Column(db.String(255), unique=True)
	difficulty = db.Column(db.Integer)
	image_link = db.Column(db.String(255))

	def __init__(self, user_id, name, time, difficulty, image_link) -> None:
		super().__init__()
		self.user_id = user_id
		self.name = name
		self.time = time
		self.image_link = image_link

	
	@staticmethod
	def create(user_id, name, time, difficulty):
		recipe = Recipe(
			user_id = user_id,
			name = name,
			time = time,
			difficulty = difficulty,
			image_link = None,
		)
		db.session.add(recipe)
		db.session.commit()
		return recipe

	@staticmethod
	def deleteById(recipe_id):
		recipe = Recipe.query.filter_by(recipe_id=recipe_id).first()
		db.session.delete(recipe)
		db.session.commit()