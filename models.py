# models.py
from extensions import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120), unique=True, primary_key=True)
    phone = db.Column(db.String(15), unique=True)
    message = db.Column(db.String(1000), unique=True)
    gender = db.Column(db.String(100), unique=True)
    nationality = db.Column(db.String(100), unique=True)
    address = db.Column(db.String(100), unique=True)

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "message": self.message,
            "gender": self.gender,
            "nationality": self.nationality,
            "address": self.address
        }
    
class CyberComplaint(db.Model):
    __tablename__ = 'cyber_complaints'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.Text)
    gender = db.Column(db.Text)
    dob = db.Column(db.Date)
    address = db.Column(db.Text)
    email = db.Column(db.Text)
    mobile = db.Column(db.Text)
    id_proof = db.Column(db.Text)
    crime_types = db.Column(db.Text)
    incident_datetime = db.Column(db.DateTime)
    platform = db.Column(db.Text)
    description = db.Column(db.Text)
    evidence = db.Column(db.Text)
    accused_name = db.Column(db.Text)
    accused_contact = db.Column(db.Text)
    accused_profile = db.Column(db.Text)
    place = db.Column(db.Text)
    signature = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "gender": self.gender,
            "dob": self.dob,
            "address": self.address,
            "email": self.email,
            "mobile": self.mobile,
            "id_proof": self.id_proof,
            "crime_types": self.crime_types,
            "incident_datetime": self.incident_datetime,
            "platform": self.platform,
            "description": self.description,
            "evidence": self.evidence,
            "accused_name": self.accused_name,
            "accused_contact": self.accused_contact,
            "accused_profile": self.accused_profile,
            "place": self.place,
            "signature": self.signature,
        }
    
class CriminalComplaint(db.Model):
    __tablename__ = 'criminal_complaints'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.Text)
    crime_type = db.Column(db.Text)
    description = db.Column(db.Text)
    location = db.Column(db.Text)
    contact = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "crime_type": self.crime_type,
            "description": self.description,
            "location": self.location,
            "contact": self.contact
        }
class PropertyRegistration(db.Model):
    __tablename__ = 'property_registration'
    id = db.Column(db.Integer, primary_key=True)
    property_type = db.Column(db.Text)
    property_address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    postal_code = db.Column(db.Text)
    property_id = db.Column(db.Text)
    area = db.Column(db.Text)
    owner_name = db.Column(db.Text)
    dob = db.Column(db.Date)
    nationality = db.Column(db.Text)
    phone = db.Column(db.Text)
    email = db.Column(db.Text)
    res_address = db.Column(db.Text)
    coowner_name = db.Column(db.Text)
    coowner_relationship = db.Column(db.Text)
    coowner_phone = db.Column(db.Text)
    coowner_email = db.Column(db.Text)
    seller_name = db.Column(db.Text)
    seller_contact = db.Column(db.Text)
    sale_date = db.Column(db.Date)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "property_type": self.property_type,
            "property_address": self.property_address,
            "city": self.city,
            "state": self.state,
            "postal_code": self.postal_code,
            "property_id": self.property_id,
            "area": self.area,
            "owner_name": self.owner_name,
            "dob": self.dob,
            "nationality": self.nationality,
            "phone": self.phone,
            "email": self.email,
            "res_address": self.res_address,
            "coowner_name": self.coowner_name,
            "coowner_relationship": self.coowner_relationship,
            "coowner_phone": self.coowner_phone,
            "coowner_email": self.coowner_email,
            "seller_name": self.seller_name,
            "seller_contact": self.seller_contact,
            "sale_date": self.sale_date,
            "submitted_at": self.submitted_at
        }