from flask import Flask, render_template, request, redirect, jsonify
from extensions import db
from datetime import datetime
import psycopg2
import logging
from flask_cors import CORS
from api.user_route import user_bp 

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Kanna_0744@localhost/naiyo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True

db.init_app(app)
app.register_blueprint(user_bp)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_db_connection():
    return psycopg2.connect(
        host='localhost',
        database='naiyo',
        user='postgres',
        password='Kanna_0744'
    )

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        gender = request.form['gender']
        nationality = request.form['nationality']
        address = request.form['address']

        logger.debug(f"Received: {name}, {email}, {phone}, {message}, {gender}, {nationality}, {address}")

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (name, email, phone, message, gender, nationality, address) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                    (name, email, phone, message, gender, nationality, address))
        conn.commit()
        cur.close()
        conn.close()

        return redirect('/')
    
    except Exception as e:
        logger.exception("Error in /submit")
        return f"Internal Server Error: {e}", 500
    
@app.route('/submit-complaint', methods=['POST'])
def submit_complaint_json():
    try:
        data = request.get_json()
        full_name = data.get('full_name')
        gender = data.get('gender')
        dob = data.get('dob')
        address = data.get('address')
        email = data.get('email')
        mobile = data.get('mobile')
        id_proof = data.get('id_proof')
        crime_types = ', '.join(data.get('crime_types', []))
        incident_datetime = data.get('incident_datetime')
        platform = data.get('platform')
        description = data.get('description')
        evidence = data.get('evidence')
        accused_name = data.get('accused_name')
        accused_contact = data.get('accused_contact')
        accused_profile = data.get('accused_profile')
        place = data.get('place')
        signature = data.get('signature')

        logger.debug(f"Received: {full_name}, {gender}, {dob}, {address}, {email}, {mobile}, {id_proof}, {crime_types}, {incident_datetime}, {platform}, {description}, {evidence}, {accused_name}, {accused_contact}, {accused_profile}, {place}, {signature}")
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO cyber_complaints (full_name, gender, dob, address, email, mobile, id_proof, crime_types, incident_datetime, platform, description, evidence, accused_name, accused_contact, accused_profile, place, signature) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (full_name, gender, dob, address, email, mobile, id_proof, crime_types, incident_datetime, platform, description, evidence, accused_name, accused_contact, accused_profile, place, signature))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'Complaint submitted successfully!'}), 200
    except Exception as e:
        logger.exception("Error in /submit-complaint")
        return f"Internal Server Error: {e}", 500
    
@app.route("/criminal-law-complaint", methods=["POST"])
def criminal_law_complaint():
    try:
        data = request.get_json()
        full_name = data.get("full_name")
        crime_type = data.get("crime_type")
        description = data.get("description")
        location = data.get("location")
        contact = data.get("contact")

        logger.debug(f"Received: {full_name}, {crime_type}, {description}, {location}, {contact}")
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO criminal_complaints (full_name, crime_type, description, location, contact) VALUES (%s, %s, %s, %s, %s)',
                        (full_name, crime_type, description, location, contact))
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "Complaint submitted successfully"}), 200
    except Exception as e:
        logger.exception("Error in /criminal-law-complaint")
        return f"Internal Server Error: {e}", 500
    
@app.route("/property-registration", methods=["POST"])
def property_registration():
    try:
        data = request.get_json()
        property_type = data.get('property_type')
        property_address = data.get('property_address')
        city = data.get('city')
        state = data.get('state')
        postal_code = data.get('postal_code')
        property_id = data.get('property_id')
        area = data.get('area') 
        owner_name = data.get('owner_name')
        dob = data.get('dob')
        nationality = data.get('nationality')
        phone = data.get('phone')
        email = data.get('email')
        res_address = data.get('res_address')
        coowner_name = data.get('coowner_name')
        coowner_relationship = data.get('coowner_relationship')
        coowner_phone = data.get('coowner_phone')
        coowner_email = data.get('coowner_email')
        seller_name = data.get('seller_name')
        seller_contact = data.get('seller_contact')
        sale_date = data.get('sale_date')

        logger.debug(f"Received: {property_type}, {property_address}, {city}, {state}, {postal_code}, {property_id}, {area}, {owner_name}, {dob}, {nationality}, {phone}, {email}, {res_address}, {coowner_name}, {coowner_relationship}, {coowner_phone}, {coowner_email}, {seller_name}, {seller_contact}, {sale_date}")
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO property_registration (property_type, property_address, city, state, postal_code, property_id, area, owner_name, dob, nationality, phone, email, res_address, coowner_name, coowner_relationship, coowner_phone, coowner_email, seller_name, seller_contact, sale_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (property_type, property_address, city, state, postal_code, property_id, area, owner_name, dob, nationality, phone, email, res_address, coowner_name, coowner_relationship, coowner_phone, coowner_email, seller_name, seller_contact, sale_date))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Property registration submitted successfully"}), 200
    except Exception as e:
        logger.exception("Error in /property-registration")
        return f"Internal Server Error: {e}", 500
        

if __name__ == "__main__":
    app.run(debug=True)

    


