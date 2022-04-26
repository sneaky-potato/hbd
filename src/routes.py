from flask import Blueprint, jsonify, request
from src.models.init_db import db
from src.models.models import Birthday

route_blueprint = Blueprint('route_blueprint', __name__)

@route_blueprint.route('/')
def api():
     return jsonify({'data': 'API is working'}), 200

@route_blueprint.route('/birthday', methods = ['GET'])
def get_birthdays():
    birthdays = Birthday.query.all()
    print(birthdays)
    return jsonify({'data': [birthday.serialize for birthday in birthdays]}), 200

@route_blueprint.route('/birthday', methods = ['POST'])
def post_birthday():
    data = request.get_json()
    try:
        name, bday_day, bday_month = data['name'], data['bday_day'], data['bday_month']
        birthday = Birthday(name=name, bday_day=bday_day, bday_month=bday_month)
        db.session.add(birthday)
        db.session.commit()
        return jsonify({'data': 'success'}), 200

    except KeyError:
        return jsonify({'data': 'failure', 'details': 'check request body'}), 400