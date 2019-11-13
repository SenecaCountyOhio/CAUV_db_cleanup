from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///CAUV_CHECK.sqlite3'
    db.init_app(app)

    with app.app_context():
        # Imports
        from . import routes
        from . import models

        # Create tables for our models
        db.create_all()
        return app
