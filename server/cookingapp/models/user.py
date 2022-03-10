from .. import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
	"""User account model."""
	__tablename__ = "user"

	user_id = db.Column(db.Integer(), primary_key = True)
	google_id = db.Column(db.String(255))
	name = db.Column(db.String(255))
	email = db.Column(db.String(255))
	profile_pic = db.Column(db.Text())
	password = db.Column(db.String(255))

	recipe = db.relationship('Recipe', backref = "user")

	def __init__(self, google_id, name, email, profile_pic, password) -> None:
		super().__init__()
		self.google_id = google_id
		self.name = name
		self.email = email
		self.profile_pic = profile_pic
		self.password = generate_password_hash(password, method='sha256')

	def __repr__(self):
		return self.name

	@staticmethod
	def create(name, email, password):
		user = User(
			google_id = None,
			profile_pic = None,
			name = name,
			email = email,
			password = password,
		)
		db.session.add(user)
		db.session.commit()
		return user

	def get_id(self):
		return self.user_id

	@classmethod
	def authenticate(cls, email, password):

		if not email or not password:
			return None
		user = cls.query.filter_by(email=email).first()
		if not user or not check_password_hash(user.password, password):
			return None
		return user
