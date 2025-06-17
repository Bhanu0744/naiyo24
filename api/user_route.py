from flask import Blueprint, request, jsonify
from models import User, CyberComplaint, CriminalComplaint, PropertyRegistration, LegalComplaint
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

@user_bp.route('/cyber-complaints', methods=['GET'])
def get_cyber_complaints():
    complaints = CyberComplaint.query.all()
    return jsonify([complaint.to_dict() for complaint in complaints])

@user_bp.route('/cyber-complaints', methods=['POST'])
def create_cyber_complaint():
    data = request.get_json()
    new_complaint = CyberComplaint(
        full_name=data['full_name'],
        gender=data['gender'],
        dob=data['dob'],
        crime_types=data['crime_types'],
        incident_datetime=data['incident_datetime'],
        platform=data['platform'],
        description=data['description'],
        evidence=data['evidence'],
        accused_name=data['accused_name'],
        accused_contact=data['accused_contact'],
        address=data['address'],
        email=data['email'],
        mobile=data['mobile'],
        id_proof=data['id_proof'],
        place=data['place'],
        signature=data['signature']
    )
    db.session.add(new_complaint)
    db.session.commit()
    return jsonify(new_complaint.to_dict()), 201

@user_bp.route('/criminal-complaints', methods=['GET'])
def get_criminal_complaints():
    complaints = CriminalComplaint.query.all()
    return jsonify([complaint.to_dict() for complaint in complaints])

@user_bp.route('/criminal-complaints', methods=['POST'])
def create_criminal_complaint():
    data = request.get_json()
    new_complaint = CriminalComplaint(
        full_name=data['full_name'],
        crime_type=data['crime_type'],
        description=data['description'],
        location=data['location'],
        contact=data['contact']
    )
    db.session.add(new_complaint)
    db.session.commit()
    return jsonify(new_complaint.to_dict()), 201

@user_bp.route('/property-registration', methods=['GET'])
def get_property_registration():
    registrations = PropertyRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/property-registration', methods=['POST'])
def create_property_registration():
    try:
        data = request.get_json()
        # dob = datetime.strptime(data['dob'], "%Y-%m-%d").date() if data.get('dob') else None
        # sale_date = datetime.strptime(data['sale_date'], "%Y-%m-%d").date() if data.get('sale_date') else None

        new_registration = PropertyRegistration(
            property_type=data['property_type'],
            property_address=data['property_address'],
            city=data['city'],
            state=data['state'],
            postal_code=data['postal_code'],
            property_id=data['property_id'],
            area=data['area'],
            owner_name=data['owner_name'],
            dob=data['dob'],
            nationality=data['nationality'],
            phone=data['phone'],
            email=data['email'],
            res_address=data['res_address'],
            coowner_name=data['coowner_name'],
            coowner_relationship=data['coowner_relationship'],
            coowner_phone=data['coowner_phone'],
            coowner_email=data['coowner_email'],
            seller_name=data['seller_name'],
            seller_contact=data['seller_contact'],
            sale_date=data['sale_date']
        )

        db.session.add(new_registration)
        db.session.commit()

        return jsonify(new_registration.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@user_bp.route('/legal-complaint', methods=['GET'])
def get_legal_complaint():
    complaints = LegalComplaint.query.all()
    return jsonify([complaint.to_dict() for complaint in complaints])

@user_bp.route('/legal-complaint', methods=['POST'])
def create_legal_complaint():
    data = request.get_json()
    new_complaint = LegalComplaint(
        case_no=data['case_no'],
        complainant_name=data['complainant_name'],
        complainant_address=data['complainant_address'],
        complainant_contact=data['complainant_contact'],
        complainant_email=data['complainant_email'],
        respondent_name=data['respondent_name'],
        respondent_address=data['respondent_address'],
        respondent_contact=data['respondent_contact'],
        respondent_email=data['respondent_email'],
        relevant_act=data['relevant_act'],
        complainant_full_name=data['complainant_full_name'],
        complainant_full_address=data['complainant_full_address'],
        complainant_contact_details=data['complainant_contact_details'],
        respondent_full_name=data['respondent_full_name'],
        respondent_full_address=data['respondent_full_address'],
        respondent_contact_details=data['respondent_contact_details'],
        facts=data['facts'],
        cause_of_action=data['cause_of_action'],
        relief_sought=data['relief_sought'],
        documents=data['documents'],
        place=data['place'],
        date_filed=data['date_filed'],
        verified_by=data['verified_by'],
        verified_date=data['verified_date']
    )

    db.session.add(new_complaint)
    db.session.commit()

    return jsonify(new_complaint.to_dict()), 201



