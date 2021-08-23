from flask_wtf import FlaskForm, Form
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, SelectField, IntegerField, RadioField, FieldList, FormField, TimeField, FileField
from wtforms.validators import  DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileAllowed


class RegisterForm(FlaskForm):
	pseudo = StringField(
		"nom d'utilisateur",
		[DataRequired(),
		Length(max=255, message=("nom d'utilisateur trop long."))]
	)
	email = StringField(
		'email',
		[
			Length(min=6),
			Email(message=("l'adresse mail n'est pas valide.")),
			DataRequired()
		]
	)
	password = PasswordField(
		'mot de passe',
		[
			DataRequired("veuillez entrer un mot de passe."),
			Length(min=6, message=('votre mot de passe est trop court.'))
		]
	)
	confirmPassword = PasswordField(
		'répétez le mot de passe',
		[
			DataRequired(),
			EqualTo('password', message='les mots de passes ne sont pas les mêmes.')
		]
	)
	# recaptcha = RecaptchaField()
	submit = SubmitField('Valider')

class LoginForm(FlaskForm):
	"""User Log-in Form."""
	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email(message='entrer une adresse mail valide')
		]
	)
	password = PasswordField('mot de passe', validators=[DataRequired()])
	submit = SubmitField('Se Connecter')


class IngredientForm(FlaskForm):
	"""Subform

	CSRF is disabled for this subform
	because it is never used by itself.
	"""
	class Meta:
		csrf = False

	ing_name = StringField(
		'ingrédient',
		validators=[DataRequired(), Length(max=255)]
	)
	quantity = IntegerField(
		'quantité',
		validators=[DataRequired()]
	)
	unity = SelectField(
		'unité', 
		choices=[(0, 'unité'), (1, 'g'), (2, 'mL'), (3, 'cL')]
	)

class StepForm(FlaskForm):
	"""Subform

	CSRF is disabled for this subform
	because it is never used by itself.
	"""
	class Meta:
		csrf = False
	
	step_text = TextAreaField('étape')

class RecipeForm(FlaskForm):
	"""Parent form"""
	name = StringField(
		'nom de la recette',
		validators=[
			DataRequired()
		]
	)
	difficulty = RadioField(
		'difficulté',
		choices=[(0, 'facile'), (1, 'moyen'), (2, 'difficile')]
	)
	time_ = TimeField(
		'temps requis'
	)
	ingredients = FieldList(
		FormField(IngredientForm),
		min_entries=1
	)
	steps = FieldList(
		FormField(StepForm),
		min_entries=1
	)
	photo = FileField(
		'photo',
		validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'images seulement au format jpg ou png')]
	)
	submit = SubmitField('Valider')

class ModifyTitleForm(FlaskForm):
	name = StringField(
		'nouveau nom',
		validators=[
			DataRequired()
		]
	)
	submit_title = SubmitField('Valider')

class ModifyImageForm(FlaskForm):
	photo = FileField(
		'photo',
		validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'images seulement au format jpg ou png')]
	)
	submit_image = SubmitField('Valider')

class ModifyStepForm(FlaskForm):
	step_text = TextAreaField('étape')
	submit_step = SubmitField('Valider')


class ModifyIngredientForm(FlaskForm):
	ing_name = StringField(
		'ingrédient',
		validators=[DataRequired(), Length(max=255)]
	)
	quantity = IntegerField(
		'quantité',
		validators=[DataRequired()]
	)
	unity = SelectField(
		'unité', 
		choices=[(0, 'unité'), (1, 'g'), (2, 'mL'), (3, 'cL')]
	)
	submit_ingredient = SubmitField('Valider')