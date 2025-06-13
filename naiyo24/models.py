# models.py
from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    name = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(120), unique=True, primary_key=True)
    phone = db.Column(db.String(15), unique=True)
    message = db.Column(db.String(1000), unique=True)

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "message": self.message
        }
    
class Regist(db.Model):
    __tablename__ = 'list'
    name = db.Column(db.String(100), unique=True, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(15), unique=True)
    aadhar = db.Column(db.String(12), unique=True)
    how = db.Column(db.String(1000), unique=True)

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "aadhar": self.aadhar,
            "how": self.how
        }
