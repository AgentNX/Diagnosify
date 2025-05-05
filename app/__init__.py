from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_migrate import Migrate

# Initializing extensions
db = SQLAlchemy()  # For interacting with the database using SQLAlchemy ORM
limiter = Limiter(get_remote_address)  # To limit the rate of requests from a given client
migrate = Migrate()  # To handle database migrations using Flask-Migrate

def create_app():
    """
    Factory function to create and configure the Flask application instance.

    - Configures app settings from the "config.Config" object.
    - Initializes extensions: SQLAlchemy, Flask-Limiter, and Flask-Migrate.
    - Registers the main blueprint for routing.

    Returns:
        app: A fully configured Flask application instance.
    """
    app = Flask(__name__, template_folder='templates')  # Create the Flask app, specifying the templates folder
    app.config.from_object("config.Config")  # Load configuration from the Config class defined in config.py

    # Initialize extensions with the Flask app
    db.init_app(app)  # Initialize SQLAlchemy with the app
    migrate.init_app(app, db)  # Initialize Flask-Migrate with the app and SQLAlchemy instance
    limiter.init_app(app)  # Initialize Flask-Limiter with the app

    # Import the main blueprint (defined in routes.py)
    from app.routes.routes import main
    app.register_blueprint(main)  # Register the blueprint for routing

    return app
