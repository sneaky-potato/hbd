import os
from flask import Flask

config_filename = os.path.abspath(os.path.dirname(__file__)) + "/../config.py"

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    register_blueprints(app)
    initialize_database(app)
    initialize_celery(app)
    # celery.conf.update(app.config)

    return app

def register_blueprints(app):
    from src.routes.birthdays import route_blueprint

    app.register_blueprint(route_blueprint)

def initialize_database(app):
    from src.models import db

    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)

def initialize_celery(app):
    from src.worker import celery

    celery.conf.update(app.config)

app = create_app()