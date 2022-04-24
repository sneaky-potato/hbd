import os
from flask import Flask
from src.models import db
from src.routes.birthdays import route_blueprint

config_filename = os.path.abspath(os.path.dirname(__file__)) + "/../config.py"

app = Flask(__name__)
app.config.from_pyfile(config_filename)
app.register_blueprint(route_blueprint)

db.init_app(app)
with app.app_context():
    db.create_all(app=app)
