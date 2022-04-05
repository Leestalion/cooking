"""Routes for user authentification."""
from flask import Blueprint, jsonify, redirect, url_for, request, current_app as app
from flask_login import login_user
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from ..schemas.schemas import user_schema
from cookingapp.utils.helpers import get_google_provider_cfg
from ..utils.helpers import client
from .. import db
from ..models.user import User
import json
import requests


ERROR_NO_EMAIL = 400
ERROR_NO_PASSWORD = 401
ERROR_NO_USER_FOUND_WITH_EMAIL = 402
ERROR_NO_NAME = 403
EMAIL_ALREADY_IN_USE = 404
NAME_ALREADY_IN_USE = 405
WRONG_CREDENTIALS = 406


# Blueprint Configuration
auth_bp = Blueprint(
	'auth_bp', __name__,
	template_folder = 'templates',
	static_folder='static'
)

@auth_bp.route('/login', methods=['POST'])
def login():
	"""
	Login : send the JWT token with the user corresponding to the demanded user.
	"""

	# get requests objects 

	data = request.get_json()
	email = data['email']
	password = data['password']

	if not email:
		return jsonify({"error": ERROR_NO_EMAIL}), 200
	if not password:
		return jsonify({"error": ERROR_NO_PASSWORD}), 200

	existing_user_mail = User.query.filter_by(email = email).first()
	if (not existing_user_mail):
		return jsonify({"error": ERROR_NO_USER_FOUND_WITH_EMAIL}), 200

	user = User.authenticate(email, password)

	if not user:
		return jsonify({'error': WRONG_CREDENTIALS}), 200

	access_token = create_access_token(identity = user.get_id())
	response = jsonify({'access_token': access_token, 'user': user_schema.dump(user)})
	return response, 200


@auth_bp.route("/logout", methods=['POST'])
def logout():
	return jsonify({'success': 'logged out'}), 200

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
	# access the identity of the current user with get_jwt_identity
	current_user = get_jwt_identity()
	return jsonify(logged_in_as = current_user), 200


@auth_bp.route('/login/callback/', methods=["GET", "POST"])
def callback():
	# Get authorization code Google sent back
	code = request.args.get("code")
	# Find what URL to hit to get tokens that allow you to ask
	# for things on behalf of a user
	google_provider_cfg = get_google_provider_cfg()
	token_endpoint = google_provider_cfg["token_endpoint"]
	# Prepare and send a request to get tokens
	token_url, headers, body = client.prepare_token_request(
		token_endpoint,
		authorization_response=request.url,
		redirect_url=request.base_url,
		code=code
	)
	try:
		token_response = requests.post(
			token_url,
			headers=headers,
			data=body,
			auth=(app.config["GOOGLE_CLIENT_ID"], app.config["GOOGLE_CLIENT_SECRET"]),
		)
	except Exception as error:
		print(error)
	# Parse the tokens
	try:
		client.parse_request_body_response(json.dumps(token_response.json()))
	except Exception as error:
		print(error)
	# hit the URL from Google that gives the user's profile info
	userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
	uri, headers, body = client.add_token(userinfo_endpoint)
	userinfo_response = requests.get(uri, headers=headers, data=body)
	# verify email
	if userinfo_response.json().get("email_verified"):
		unique_id = userinfo_response.json()["sub"]
		users_email = userinfo_response.json()["email"]
		picture = userinfo_response.json()["picture"]
		users_name = userinfo_response.json()["given_name"]
	else:
		return "User email not available or not verified by Google.", 400
	
	user = User(unique_id, users_name, users_email, picture)
	temp = User.query.filter_by(user_id=unique_id).first()
	if not temp :
		# if user does not exists, login user
		User.create(unique_id, users_name, users_email, picture)
	
	# Login
	login_user(user)

	# send user back to homepage
	return redirect(url_for('main_bp.index'))
	



@auth_bp.route('/register', methods=['POST'])
def register():
	"""
	User register.
	"""

	# Get Request objects
	data = request.get_json()
	email = data['email']
	name = data['name']
	password = data['password']

	if not email:
		return jsonify({"error": ERROR_NO_EMAIL}), 200
	if not password:
		return jsonify({"error": ERROR_NO_PASSWORD}), 200
	if not name:
		return jsonify({"error": ERROR_NO_NAME}), 200

	existing_user_mail = User.query.filter_by(email = email).first()
	if (existing_user_mail):
		return jsonify({"error": EMAIL_ALREADY_IN_USE}), 200

	existing_user_name = User.query.filter_by(name = name).first()
	if (existing_user_name):
		return jsonify({"error": NAME_ALREADY_IN_USE}), 200

	user = User.create(name=name, email=email, password=password)

	access_token = create_access_token(identity = user.get_id())
	response = jsonify({'access_token': access_token, 'user': user_schema.dump(user)})
	return response, 200