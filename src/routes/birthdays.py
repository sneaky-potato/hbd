from flask import Blueprint, jsonify, request
from src.models.birthday import Birthday
from src.models import db

route_blueprint = Blueprint('route_blueprint', __name__)

@route_blueprint.route('/')
def api():
     return jsonify({'data': 'API is working'}), 200

@route_blueprint.route('/birthday', methods = ['GET'])
def get_birthdays():
    birthdays = Birthday.query.all()
    return jsonify({'data': birthdays}), 200

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