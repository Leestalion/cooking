from os import path
from flask import Blueprint, flash, current_app as app, jsonify
from flask import render_template, url_for, redirect, request
from flask_login import current_user, login_required, logout_user
from flask_jwt_extended import jwt_required, get_jwt_identity
import jwt

from cookingapp.utils.helpers import upload_file_to_s3
from ..utils.forms import RecipeForm, IngredientForm, StepForm, ModifyTitleForm, ModifyImageForm, ModifyStepForm, ModifyIngredientForm, TestForm
from ..models.user import User
from ..models.recipe import Recipe
from ..models.recipe_ingredient import RecipeIngredient
from ..models.ingredient import Ingredient
from ..models.step import Step
from ..schemas.schemas import ingredient_schema, ingredients_schema, recipe_schema, recipes_schema
from werkzeug.utils import secure_filename
from .. import db



ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
NOT_LOGGED_ERROR = 100
ERROR_NO_INGREDIENT = 600
ERROR_INGREDIENT_ALREADY_EXISTS = 601
ERROR_NO_NAME = 602
ERROR_RECIPE_ALREADY_EXIST = 603



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



@main_bp.route("/addrecipe", methods=['POST'])
@jwt_required()
def addrecipe():

	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({"error": NOT_LOGGED_ERROR})


	# Get Request objects
	data = request.get_json()
	name = data['name']
	difficulty = data['difficulty']
	time = data['time']
	steps = data['steps']
	ingredients = data['ingredients']

	if not name:
		return jsonify({"error": ERROR_NO_NAME}), 200

	existing_recipe_name = Recipe.query.filter_by(name = name).first()
	if (existing_recipe_name):
		return jsonify({"error": ERROR_RECIPE_ALREADY_EXIST}), 200

	recipe = Recipe.create(user_id = current_user, name=name, difficulty=difficulty, time=time)

	for ingredient in ingredients:
		RecipeIngredient.create(recipe.recipe_id, ingredient["id"], ingredient["quantity"], ingredient["unity"])

	for step in steps:
		Step.create(recipe_id=recipe.recipe_id, step_text=step["text"])

	response = jsonify({'recipe': recipe_schema.dump(recipe)})
	return response, 200



@main_bp.route('/recipes', methods=["POST"])
def getrecipes():
	return jsonify({'recipes': recipes_schema.dump(Recipe.query.all())}), 200



@main_bp.route('/current-user-recipes', methods=["POST"])
@jwt_required()
def getCurrentUserRecipes():

	current_user = get_jwt_identity()
	if not current_user:
		return jsonify({"error": NOT_LOGGED_ERROR})

	return jsonify({'recipes': recipes_schema.dump(Recipe.query.filter_by(user_id=current_user))})



@main_bp.route('/delete-recipe', methods=["POST"])
@jwt_required()
def deleteRecipe():
	data = request.get_json()
	recipe_id = data['id']

	if not recipe_id:
		return jsonify({'error': "no recipe ID found"})

	RecipeIngredient.deleteByRecipeId(recipe_id=recipe_id)
	Step.deleteByRecipeId(recipe_id=recipe_id)

	Recipe.deleteById(recipe_id=recipe_id)
	return jsonify({'success': True})


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

@main_bp.route('/addingredient', methods=["POST"])
@jwt_required()
def addIngredient():

	data = request.get_json()
	ingredient_name = data['name']
	unity = data['unity']
	
	if not ingredient_name:
		return jsonify({"error": ERROR_NO_INGREDIENT}), 200
	
	existing_ingredient = Ingredient.query.filter_by(ingredient_name = ingredient_name).first()
	if existing_ingredient:
		return jsonify({"error": ERROR_INGREDIENT_ALREADY_EXISTS}), 200

	ingredient = Ingredient.create(ingredient_name=ingredient_name, unity = unity)
	
	return jsonify({'ingredient': ingredient_schema.dump(ingredient)}), 200

@main_bp.route('/ingredients', methods=['GET'])
@jwt_required()
def getIngredients():
	return jsonify({'ingredients': ingredients_schema.dump(Ingredient.query.all())}), 200


def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS