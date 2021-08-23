"""Routes for user authentification."""
from flask import Blueprint, render_template, request, redirect, flash, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from .forms import RegisterForm, LoginForm
from .models import db, User
from . import login_manager

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

	form = LoginForm()
	# Validate login attempt
	if form.validate_on_submit():
		print("start")
		user = User.query.filter_by(email=form.email.data).first()
		if user and user.check_password(password=form.password.data):
			login_user(user)
			return redirect(url_for('main_bp.index'))
		flash('combinaison email/mot de pass inconnue')
	return render_template("login.html", form=form)


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