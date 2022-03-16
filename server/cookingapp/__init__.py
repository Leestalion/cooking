from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_wtf.csrf import generate_csrf
from flask_cors import CORS
from sqlalchemy import true
from flask_jwt_extended import JWTManager

# Globally accessible libraries
db = SQLAlchemy()
csrf = CSRFProtect()
cors = CORS()
jwt =  JWTManager()

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, 
        instance_relative_config=True
    )
    app.config.from_object('config.Config')
    # Initialize Plugins
    csrf.init_app(app)
    db.init_app(app)
    cors.init_app(app, supports_credentials = True)
    jwt.init_app(app)

    @app.after_request
    def set_csrf_cookie(response):
        response.set_cookie('XSRF-TOKEN', generate_csrf())
        return response

    with app.app_context():
        # Include our Routes
        from .routes import routes
        from .routes import auth

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        # Create Database Models
        db.create_all()

        return app