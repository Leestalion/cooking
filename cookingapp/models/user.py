from .. import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
	"""User account model."""
	__tablename__ = "user"

	user_id = db.Column(db.String(255), primary_key = True)
	name = db.Column(db.String(255))
	email = db.Column(db.String(255))
	profile_pic = db.Column(db.Text())

	recipe = db.relationship('Recipe', backref = "user")

	def __init__(self, user_id, name, email, profile_pic) -> None:
		super().__init__()
		self.user_id = user_id
		self.name = name
		self.email = email
		self.profile_pic = profile_pic

	def __repr__(self):
		return self.name

	@staticmethod
	def create(user_id, name, email, profile_pic):
		user = User(
			user_id = user_id,
			name = name,
			email = email,
			profile_pic = profile_pic
		)
		db.session.add(user)
		db.session.commit()

	def get_id(self):
		return self.user_id
