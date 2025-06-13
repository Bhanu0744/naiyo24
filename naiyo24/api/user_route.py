from flask import Blueprint, request, jsonify
from models import User
from extensions import db  

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], phone=data['phone'], message=data['message'], gender=data['gender'], nationality=data['nationality'], address=data['address'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201