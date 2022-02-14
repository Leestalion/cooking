from base64 import encode
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

DEVELOPMENT='development'
PRODUCTION='production'

class Config:
	"""Set Flask configuration from .env file."""

	# General Config
	SECRET_KEY = environ.get('SECRET_KEY')
	FLASK_APP = environ.get('FLASK_APP')
	FLASK_ENV = environ.get('FLASK_ENV')

	UPLOAD_FOLDER = path.join(basedir, 'cookingapp/static/media')

    # MYSQL database parameters
	if(FLASK_ENV == DEVELOPMENT):
		MYSQL_HOST =  environ.get('MYSQL_HOST_DEVELOPMENT')
		MYSQL_USER = environ.get("MYSQL_USER_DEVELOPMENT")
		MYSQL_PASSWORD = environ.get("MYSQL_PASSWORD_DEVELOPMENT")
		MYSQL_DB =  environ.get('MYSQL_DB_DEVELOPMENT')
	elif (FLASK_ENV == PRODUCTION):
		MYSQL_HOST =  environ.get('MYSQL_HOST_PROD')
		MYSQL_USER = environ.get("MYSQL_USER_PROD")
		MYSQL_PASSWORD = environ.get("MYSQL_PASSWORD_PROD")
		MYSQL_DB =  environ.get('MYSQL_DB_PROD')

	# SQL Alchemy parameters
	SQLALCHEMY_ECHO = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = "mysql://"+MYSQL_USER+":"+MYSQL_PASSWORD+"@"+MYSQL_HOST+"/"+MYSQL_DB

	# AWS parameters
	AWS_SECRET_ACCESS_KEY = environ.get("AWS_SECRET_ACCESS_KEY")
	AWS_ACCESS_KEY = environ.get("AWS_ACCESS_KEY")
	AWS_BUCKET_NAME = environ.get("AWS_BUCKET_NAME")

	# Google parameters
	GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID")
	GOOGLE_CLIENT_SECRET = environ.get("GOOGLE_CLIENT_SECRET")
	GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
