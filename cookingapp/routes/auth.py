"""Routes for user authentification."""
from flask import Blueprint, render_template, redirect, flash, url_for, request, current_app as app
from flask_login import current_user, login_user

from cookingapp.utils.helpers import get_google_provider_cfg
from ..utils.forms import RegisterForm
from ..utils.helpers import client
from .. import db
from ..models.user import User
from .. import login_manager
import json
import requests

# Blueprint Configuration
auth_bp = Blueprint(
	'auth_bp', __name__,
	template_folder = 'templates',
	static_folder='static'
)

@auth_bp.route('/login/', methods=['GET', 'POST'])
def login():
	"""
	Login page for registered users.

	GET requests serve login page
	POST requests validate and redirect user to index.
	"""
	# Bypass if user is logged in
	if current_user.is_authenticated: 
		return redirect(url_for('main_bp.index'))

	# define Google login URL
	google_provider_cfg = get_google_provider_cfg()
	authorization_endpoint = google_provider_cfg["authorization_endpoint"]

	request_uri = client.prepare_request_uri(
		authorization_endpoint,
		redirect_uri=request.base_url+"callback/",
		scope=["openid", "https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"],
	)
	return redirect(request_uri)


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
	print(token_url, headers, body)
	try:
		token_response = requests.post(
			token_url,
			headers=headers,
			data=body,
			auth=(app.config["GOOGLE_CLIENT_ID"], app.config["GOOGLE_CLIENT_SECRET"]),
		)
	except Exception as error:
		print(error)
	print("token_response :", token_response.json())
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
	



@auth_bp.route('/register/', methods=['GET', 'POST'])
def register():
	"""
	User register page.

	GET requests serve sign-up page.
	POST requests validate form and user creation.
	"""
	form = RegisterForm()
	if form.validate_on_submit():
		existing_user_mail = User.query.filter_by(email = form.email.data).first()
		existing_user_pseudo = User.query.filter_by(pseudo = form.pseudo.data).first()
		if (existing_user_mail is None and existing_user_pseudo is None):
			user = User(
				pseudo = form.pseudo.data,
				email=form.email.data
			)
			user.set_password(form.password.data)
			db.session.add(user)
			db.session.commit()
			login_user(user)
			return redirect(url_for('main_bp.index'))
		elif (existing_user_pseudo is not None):
			flash('Un utilisateur possède déjà le même pseudo.')
		elif (existing_user_mail is not None):
			flash('Un utilisateur possède déjà la même adresse mail.')
	return render_template(
		'register.html', form=form)

@login_manager.user_loader
def load_user(user_id):
	"""Check if the user is logged in on every page load."""
	if user_id is not None:
		return User.query.get(user_id)
	return None

@login_manager.unauthorized_handler
def unauthorized():
	"""Redirect unauthorized users to Login page."""
	flash('You must be logged in to view that page.')
	return redirect(url_for('auth_bp.login'))