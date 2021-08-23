from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

SQLALCHEMY_TRACK_MODIFICATIONS = False

MYSQL_HOST = 'mysql-thomas-lemarrec.alwaysdata.net'
MYSQL_USER = '204077'
MYSQL_PASSWORD = 'ibis1234'
MYSQL_DB = 'thomas-lemarrec_cooking'

UPLOAD_FOLDER = path.join(basedir, 'cookingapp/static/media')

class Config:
	"""Set Flask configuration from .env file."""

	# General Config
	SECRET_KEY = environ.get('SECRET_KEY')
	FLASK_APP = environ.get('FLASK_APP')
	FLASK_ENV = environ.get('FLASK_ENV')

    # Database
	SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
	SQLALCHEMY_ECHO = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	SQLALCHEMY_DATABASE_URI = "mysql://"+MYSQL_USER+":"+MYSQL_PASSWORD+"@"+MYSQL_HOST+"/"+MYSQL_DB