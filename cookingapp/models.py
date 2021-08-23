from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
	"""User account model."""
	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key = True)
	password = db.Column(db.Text)
	pseudo = db.Column(db.String(255))
	email = db.Column(db.String(255))

	recipe = db.relationship('Recipe', backref = "users")

	def set_password(self, password):
		self.password = generate_password_hash(password, method='sha512')

	def check_password(self, password):
		""" Check hashed password."""
		return check_password_hash(self.password, password)

	def __repr__(self):
		return self.pseudo


class Recipe(db.Model):
	"""Stores recipes."""
	__tablename__ = 'recipes'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	time = db.Column(db.String(255))
	name = db.Column(db.String(255), unique=True)
	difficulty = db.Column(db.Integer)
	photo = db.Column(db.String(255))

class Ingredient(db.Model):
	"""Stores ingredients of a recipe."""
	__tablename__ = 'ingredients'

	id = db.Column(db.Integer, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))

	ing_name = db.Column(db.String(255))
	quantity = db.Column(db.Integer)
	unity = db.Column(db.Integer)

	# Relationship
	recipe = db.relationship(
		'Recipe',
		backref = db.backref('ingredients', lazy='dynamic', collection_class=list)
	)

class Step(db.Model):
	"""Stores steps of a recipe."""
	__tablename__ = 'steps'

	id = db.Column(db.Integer, primary_key=True)
	recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'))

	step_text = db.Column(db.String)

	# Relationship
	recipe = db.relationship(
		'Recipe',
		backref = db.backref('steps', lazy='dynamic', collection_class=list)
	)