# models.py
from extensions import db

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