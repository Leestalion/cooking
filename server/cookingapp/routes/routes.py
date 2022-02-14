from os import path
from flask import Blueprint, flash, current_app as app, jsonify
from flask import render_template, url_for, redirect
from flask_login import current_user, login_required, logout_user

from cookingapp.utils.helpers import upload_file_to_s3
from ..utils.forms import RecipeForm, IngredientForm, StepForm, ModifyTitleForm, ModifyImageForm, ModifyStepForm, ModifyIngredientForm, TestForm
from ..models.user import User
from ..models.recipe import Recipe
from ..models.recipe_ingredient import RecipeIngredient
from ..models.ingredient import Ingredient
from ..models.step import Step
from werkzeug.utils import secure_filename
from .. import db


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


main_bp = Blueprint(
	'main_bp', __name__,
	template_folder = 'templates',
	static_folder = 'static'
)

# sanity check route
@main_bp.route("/ping", methods=['GET'])
def ping_pong():
	return jsonify('pong!')

@main_bp.route("/google97a1864ac8cc98b6.html")
def google_site_verf():
    return render_template("google97a1864ac8cc98b6.html")

@main_bp.route('/', methods = ['GET'])
@main_bp.route('/index/', methods = ['GET'])
def index():
    return render_template(
    	"index.html", 
    	current_user=current_user,
    	recipes = Recipe.query
    )

@main_bp.route("/logout/")
@login_required
def logout():
	logout_user()
	return redirect(url_for('main_bp.index'))

@main_bp.route("/addrecipe/", methods=['GET', 'POST'])
@login_required
def addrecipe():
	form = RecipeForm()
	template_form_1 = IngredientForm(prefix='ingredients-_-')
	template_form_2 = StepForm(prefix='steps-_-')

	if form.validate_on_submit():
		file = form.photo.data
		if file:

			existing_recipe_name = Recipe.query.filter_by(name = form.name.data).first()
			if (existing_recipe_name is None):

				filename = secure_filename(form.photo.data.filename)
				form.photo.data.save(path.join(app.config["UPLOAD_FOLDER"], filename))

				recipe = Recipe(
					user_id = current_user.id,
					name = form.name.data,
					time = form.time_.data,
					difficulty = form.difficulty.data,
					photo = filename
				)

				db.session.add(recipe)

				for ingredient in form.ingredients.data:
					new_ingredient = RecipeIngredient(**ingredient)
					# Add to recipe
					recipe.ingredients.append(new_ingredient)

				for step in form.steps.data:
					new_step = Step(**step)
					# Add to recipe
					recipe.steps.append(new_step)

				db.session.commit()
				return redirect("/index/")

			flash("ce nom de recette est déjà pris.")

		flash("fichier introuvable")

	return render_template(
		"addrecipe.html", 
		form=form, 
		current_user=current_user,
		template1 = template_form_1,
		template2 = template_form_2
	)


@main_bp.route('/recipe/<id>', methods = ['GET'])
def recipe(id):
	recipe = Recipe.query.filter_by(id=id).first_or_404()
	return render_template(
		"recipe.html", 
		current_user=current_user,
		recipe = recipe
	)

@main_bp.route('/user/<user_id>', methods = ['GET'])
def user(user_id):
	user = User.query.filter_by(user_id=user_id).first_or_404()
	recipes = Recipe.query.filter_by(user_id=user_id)
	return render_template(
		"user.html", 
		current_user=current_user,
		user = user,
		recipes = recipes
	)

@main_bp.route('/recipe/<id>/modify/<element>', methods = ['GET', 'POST'])
@login_required
def modify(id, element):
	recipe = Recipe.query.filter_by(id=id).first_or_404()
	title_form = ModifyTitleForm()
	image_form = ModifyImageForm()
	step_form = ModifyStepForm()
	ingredient_form = ModifyIngredientForm()

	if title_form.submit_title.data and title_form.validate():
		if title_form.validate_on_submit():
			recipe.name = title_form.name.data
			db.session.commit()
			return redirect("/recipe/"+id+"/modify/success")

	if image_form.submit_image.data and image_form.validate():
		if image_form.validate_on_submit():
			filename = secure_filename(image_form.photo.data.filename)
			image_form.photo.data.save(path.join(app.config["UPLOAD_FOLDER"], filename))


			recipe.photo = filename
			db.session.commit()
			return redirect("/recipe/"+id+"/modify/success")

	if step_form.submit_step.data and step_form.validate():
		if step_form.validate_on_submit():
			#flash("on est là")
			step = Step.query.get(element)
			step.step_text = step_form.step_text.data
			db.session.commit()
			return redirect("/recipe/"+id+"/modify/success")

	if ingredient_form.submit_ingredient.data and ingredient_form.validate():
		if ingredient_form.validate_on_submit():
			flash("on est là")
			ingredient = RecipeIngredient.query.get(element)
			ingredient.ing_name = ingredient_form.ing_name.data
			ingredient.quantity = ingredient_form.quantity.data
			ingredient.unity = ingredient_form.unity.data
			db.session.commit()
			return redirect("/recipe/"+id+"/modify/success")
			

	return render_template(
		"modify.html", 
		current_user=current_user,
		recipe = recipe,
		element = element,
		title_form = title_form,
		image_form = image_form,
		step_form = step_form,
		ingredient_form = ingredient_form
	)

@main_bp.route('/test/', methods=["GET", "POST"])
def test():
	form = TestForm()

	if form.validate_on_submit():
		file = form.photo.data

		if file.filename == '':
				flash('No selected file')
				return redirect(url_for('main_bp.index'))

		# check wether the file extension is allowed (eg. png, jpeg, jpg, gif)
		if file and allowed_file(file.filename):
			output = upload_file_to_s3(file)

			# if upload success, will return file name of uploaded file
			if output:
				flash("Success upload")
				return redirect(url_for('main_bp.index'))

			# upload failed, redirect to upload page
			else:
				flash("Unable to upload, try again")
				return redirect(url_for('main_bp.index'))

	return render_template(
		"test.html",
		form = form
	)


def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
