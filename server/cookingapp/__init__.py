from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from flask_cors import CORS

# Globally accessible libraries
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
cors = CORS();

def create_app():
    """Initialize the core application."""
    app = Flask(__name__, 
        static_folder='../../client/dist/',
        static_url_path='/',
        instance_relative_config=False
    )
    app.config.from_object('config.Config')
    # Initialize Plugins
    csrf.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app, resources={r'/api*': {'origins': '*'}})

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