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