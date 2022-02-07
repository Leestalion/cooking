from .. import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
	"""User account model."""
	__tablename__ = "user"

	user_id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255))
	email = db.Column(db.String(255))
	profile_pic = db.Column(db.Text())

	recipe = db.relationship('Recipe', backref = "user")

	def __repr__(self):
		return self.name

	@staticmethod
	def create(id_, name, email, profile_pic):
		user = User(
			user_id = id_,
			name = name,
			email = email,
			profile_pic = profile_pic
		)
		db.session.add(user)
		db.session.commit()
