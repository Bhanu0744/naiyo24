from flask import Blueprint, request, jsonify
from models import User, Regist
from extensions import db  

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(name=data['name'], email=data['email'], phone=data['phone'], message=data['message'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

contact_bp = Blueprint('contact_bp', __name__)  # <-- renamed blueprint

@contact_bp.route('/contacts', methods=['POST'])  # <-- renamed endpoint
def create_contact():
    data = request.get_json()

    try:
        new_contact = Regist(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            aadhar=data['aadhar'],
            how=data['how']
        )
        db.session.add(new_contact)
        db.session.commit()
        return jsonify(new_contact.to_dict()), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


@contact_bp.route('/contacts', methods=['GET'])  # <-- renamed endpoint
def get_contacts():
    contacts = Regist.query.all()
    return jsonify([contact.to_dict() for contact in contacts])