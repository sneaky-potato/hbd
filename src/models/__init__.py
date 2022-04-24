from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from src.models.birthday import Birthday
from src.models.cars import Car