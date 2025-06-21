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

@app.route("/cybersecurity")
def cyber_complaint():
    return render_template('../html/cybersecurity.html')


@app.route('/cyber-complaint', methods=['POST'])
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


@app.route("/criminal-law")
def criminal_complaint():
    return render_template('../html/criminallaw.html')

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
    
@app.route("/property-registration")
def property_registration():
    return render_template('../html/property.html')

@app.route("/property-registration", methods=["POST"])
def submit_property_registration():
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

@app.route("/legal-complaint")
def legal_complaint():
    return render_template('../html/legal.html')

@app.route('/legal-complaint', methods=['POST'])
def submit_legal_complaint():
    try:
        data = request.get_json()
        case_no = data.get('case_no')
        complainant_name = data.get('complainant_name')
        complainant_address = data.get('complainant_address')
        complainant_contact = data.get('complainant_contact')
        complainant_email = data.get('complainant_email')
        respondent_name = data.get('respondent_name')
        respondent_address = data.get('respondent_address')
        respondent_contact = data.get('respondent_contact')
        respondent_email = data.get('respondent_email')
        relevant_act = data.get('relevant_act')
        complainant_full_name = data.get('complainant_full_name')
        complainant_full_address = data.get('complainant_full_address')
        complainant_contact_details = data.get('complainant_contact_details')
        respondent_full_name = data.get('respondent_full_name')
        respondent_full_address = data.get('respondent_full_address')
        respondent_contact_details = data.get('respondent_contact_details')
        facts = data.get('facts')
        cause_of_action = data.get('cause_of_action')
        relief_sought = data.get('relief_sought')
        documents = data.get('documents')
        place = data.get('place')
        date_filed = data.get('date_filed')
        verified_by = data.get('verified_by')
        verified_date = data.get('verified_date')

        logger.debug(f"Received: {case_no}, {complainant_name}, {complainant_address}, {complainant_contact}, {complainant_email}, {respondent_name}, {respondent_address}, {respondent_contact}, {respondent_email}, {relevant_act}, {complainant_full_name}, {complainant_full_address}, {complainant_contact_details}, {respondent_full_name}, {respondent_full_address}, {respondent_contact_details}, {facts}, {cause_of_action}, {relief_sought}, {documents}, {place}, {date_filed}, {verified_by}, {verified_date}")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO legal_complaints (case_no, complainant_name, complainant_address, complainant_contact, complainant_email, respondent_name, respondent_address, respondent_contact, respondent_email, relevant_act, complainant_full_name, complainant_full_address, complainant_contact_details, respondent_full_name, respondent_full_address, respondent_contact_details, facts, cause_of_action, relief_sought, documents, place, date_filed, verified_by, verified_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                    (case_no, complainant_name, complainant_address, complainant_contact, complainant_email, respondent_name, respondent_address, respondent_contact, respondent_email, relevant_act, complainant_full_name, complainant_full_address, complainant_contact_details, respondent_full_name, respondent_full_address, respondent_contact_details, facts, cause_of_action, relief_sought, documents, place, date_filed, verified_by, verified_date))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Legal complaint submitted successfully"}), 200
    except Exception as e:
        logger.exception("Error in /legal-complaint")
        return f"Internal Server Error: {e}", 500   
        

@app.route("/marriage-complaint")
def marriage_complaint():
    return render_template('../html/marriage.html')

@app.route('/submit-marriage-complaint', methods=['POST'])
def submit_marriage_complaint():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        complainant_name = data.get('complainant_name')
        comp_age = data.get('comp_age')
        comp_gender = data.get('comp_gender')
        comp_parent = data.get('comp_parent')
        comp_address = data.get('comp_address')
        comp_contact = data.get('comp_contact')
        comp_email = data.get('comp_email')
        spouse_name = data.get('spouse_name')
        spouse_age = data.get('spouse_age')
        spouse_gender = data.get('spouse_gender')
        spouse_parent = data.get('spouse_parent')
        spouse_address = data.get('spouse_address')
        spouse_contact = data.get('spouse_contact')
        spouse_email = data.get('spouse_email')
        marriage_date = data.get('marriage_date')
        marriage_place = data.get('marriage_place')
        marriage_type = data.get('marriage_type')
        marriage_cert_issued = data.get('marriage_cert_issued')
        marriage_reg_applied = data.get('marriage_reg_applied')
        reg_applied_date = data.get('reg_applied_date')
        complaint_nature = data.get('complaint_nature')

        logger.debug(f"Received: {id_proof}, {complainant_name}, {comp_age}, {comp_gender}, {comp_parent}, {comp_address}, {comp_contact}, {comp_email}, {spouse_name}, {spouse_age}, {spouse_gender}, {spouse_parent}, {spouse_address}, {spouse_contact}, {spouse_email}, {marriage_date}, {marriage_place}, {marriage_type}, {marriage_cert_issued}, {marriage_reg_applied}, {reg_applied_date}, {complaint_nature}")
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
                    INSERT INTO marriage_complaints (id_proof, complainant_name, comp_age, comp_gender, comp_parent, comp_address, comp_contact, comp_email, spouse_name, spouse_age, spouse_gender, spouse_parent, spouse_address, spouse_contact, spouse_email, marriage_date, marriage_place, marriage_type, marriage_cert_issued, marriage_reg_applied, reg_applied_date, complaint_nature) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, complainant_name, comp_age, comp_gender, comp_parent, comp_address, comp_contact, comp_email, spouse_name, spouse_age, spouse_gender, spouse_parent, spouse_address, spouse_contact, spouse_email, marriage_date, marriage_place, marriage_type, marriage_cert_issued, marriage_reg_applied, reg_applied_date, complaint_nature))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'Complaint submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /submit-marriage-complaint")
        return jsonify({'error': str(e)}), 500

    
@app.route("/trademark")
def trademark():
    return render_template('../html/trademark.html')

@app.route("/trademark-complaint", methods=['POST'])
def trademark_complaint():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        applicant_name = data.get('applicant_name')
        applicant_type = data.get('applicant_type')
        address = data.get('address')
        state = data.get('state')
        pin_code = data.get('pin_code')
        email = data.get('email')
        mobile = data.get('mobile')
        nationality = data.get('nationality')
        nature_of_business = data.get('nature_of_business')
        trademark_name = data.get('trademark_name')
        mark_type = data.get('mark_type')
        logo = data.get('logo')
        logo_filename = data.get('logo_filename')
        logo_mimetype = data.get('logo_mimetype')
        class_of_goods = data.get('class_of_goods')
        description = data.get('description')
        mark_used = data.get('mark_used')
        first_use_date = data.get('first_use_date')
        first_use_place = data.get('first_use_place')
        priority_claim = data.get('priority_claim')
        priority_country = data.get('priority_country')
        priority_date = data.get('priority_date')
        priority_app_no = data.get('priority_app_no')
        agent_name = data.get('agent_name')
        agent_reg_no = data.get('agent_reg_no')
        power_of_attorney = data.get('power_of_attorney')
        date = data.get('date')
        place = data.get('place')

        logger.debug(f"Received: {id_proof}, {applicant_name}, {applicant_type}, {address}, {state}, {pin_code}, {email}, {mobile}, {nationality}, {nature_of_business}, {trademark_name}, {mark_type}, {logo}, {logo_filename}, {logo_mimetype}, {class_of_goods}, {description}, {mark_used}, {first_use_date}, {first_use_place}, {priority_claim}, {priority_country}, {priority_date}, {priority_app_no}, {agent_name}, {agent_reg_no}, {power_of_attorney}, {date}, {place}")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO trademark_complaints (id_proof, applicant_name, applicant_type, address, state, pin_code, email, mobile, nationality, nature_of_business, trademark_name, mark_type, logo, logo_filename, logo_mimetype, class_of_goods, description, mark_used, first_use_date, first_use_place, priority_claim, priority_country, priority_date, priority_app_no, agent_name, agent_reg_no, power_of_attorney, date, place) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, applicant_name, applicant_type, address, state, pin_code, email, mobile, nationality, nature_of_business, trademark_name, mark_type, logo, logo_filename, logo_mimetype, class_of_goods, description, mark_used, first_use_date, first_use_place, priority_claim, priority_country, priority_date, priority_app_no, agent_name, agent_reg_no, power_of_attorney, date, place))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Complaint submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /trademark-complaint")
        return jsonify({'error': str(e)}), 500

@app.route("/barcode-form")
def barcode_form():
    return render_template("../html/barcode.html")

@app.route("/barcode-form", methods=['POST'])
def submit_barcode_form():
    try:
        data = request.get_json()
        business_name = data.get('business_name')
        contact_person = data.get('contact_person')
        address = data.get('address')
        phone = data.get('phone')
        email = data.get('email')
        gstin = data.get('gstin')
        barcode_options = data.get('barcode_options')
        barcode_format = data.get('barcode_format')
        barcode_purpose = data.get('barcode_purpose')
        declarant_name = data.get('declarant_name')
        declaration_date = data.get('declaration_date')

        logger.debug(f"Received: {business_name}, {contact_person}, {address}, {phone}, {email}, {gstin}, {barcode_options}, {barcode_format}, {barcode_purpose}, {declarant_name}, {declaration_date}")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO barcode_requests (
            business_name, contact_person, address, phone,
            email, gstin, barcode_options, barcode_format, barcode_purpose,
            declarant_name, declaration_date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data.get('business_name'),
        data.get('contact_person'),
        data.get('address'),
        data.get('phone'),
        data.get('email'),
        data.get('gstin'),
        data.get('barcode_options'),
        data.get('barcode_format'),
        data.get('barcode_purpose')
        ))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Barcode request submitted successfully!"}), 201
    except Exception as e:
        logger.exception("Error in /barcode-form")
        return f"Internal Server Error: {e}", 500

@app.route('/iso-application')
def iso_form():
    return render_template('../html/iso.html')

@app.route('/iso-application', methods=['POST'])
def submit_iso_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        org_name = data.get('org_name')
        org_type = data.get('org_type')
        address = data.get('address')
        city = data.get('city')
        state = data.get('state')
        pin = data.get('pin')
        id_proof = data.get('id_proof')
        org_name = data.get('org_name')
        org_type = data.get('org_type')
        address = data.get('address')
        city = data.get('city')
        state = data.get('state')
        pin = data.get('pin')
        country = data.get('country')
        website = data.get('website')
        establishment_year = data.get('establishment_year')
        contact_name = data.get('contact_name')
        designation = data.get('designation')
        phone = data.get('phone')
        mobile = data.get('mobile')
        email = data.get('email')
        cert_9001 = data.get('cert_9001')
        cert_14001 = data.get('cert_14001')
        cert_45001 = data.get('cert_45001')
        cert_22000 = data.get('cert_22000')
        cert_27001 = data.get('cert_27001')
        cert_other = data.get('cert_other')
        scope = data.get('scope')
        num_employees = data.get('num_employees')
        num_sites = data.get('num_sites')
        site_locations = data.get('site_locations')
        cert_iso = data.get('cert_iso')
        cert_msme = data.get('cert_msme')
        cert_gst = data.get('cert_gst')
        cert_other_name = data.get('cert_other_name')
        lang_pref = data.get('lang_pref')
        submit_date = data.get('submit_date')
        submit_place = data.get('submit_place')
        auth_name = data.get('auth_name')
        auth_designation = data.get('auth_designation')

        logger.debug(f"Received: {org_name}, {org_type}, {address}, {city}, {state}, {pin}, {country}, {website}, {establishment_year}, {contact_name}, {designation}, {phone}, {mobile}, {email}, {cert_9001}, {cert_14001}, {cert_45001}, {cert_22000}, {cert_27001}, {cert_other}, {scope}, {num_employees}, {num_sites}, {site_locations}, {cert_iso}, {cert_msme}, {cert_gst}, {cert_other_name}, {lang_pref}, {submit_date}, {submit_place}, {auth_name}, {auth_designation}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO iso_certifications (org_name, org_type, address, city, state, pin, country, website, establishment_year, contact_name, designation, phone, mobile, email, cert_9001, cert_14001, cert_45001, cert_22000, cert_27001, cert_other, scope, num_employees, num_sites, site_locations, cert_iso, cert_msme, cert_gst, cert_other_name, lang_pref, submit_date, submit_place, auth_name, auth_designation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (org_name, org_type, address, city, state, pin, country, website, establishment_year, contact_name, designation, phone, mobile, email, cert_9001, cert_14001, cert_45001, cert_22000, cert_27001, cert_other, scope, num_employees, num_sites, site_locations, cert_iso, cert_msme, cert_gst, cert_other_name, lang_pref, submit_date, submit_place, auth_name, auth_designation))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'ISO application submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /iso-application")
        return f"Internal Server Error: {e}", 500
    
@app.route('/copyright-registration')
def copyright_form():
    return render_template('../html/copy.html')

@app.route('/copyright-registration', methods=['POST'])
def submit_copyright_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        type_of_work = data.get('type_of_work')
        title = data.get('title')
        language = data.get('language')
        applicant_name = data.get('applicant_name')
        applicant_address = data.get('applicant_address')
        applicant_nationality = data.get('applicant_nationality')
        applicant_contact = data.get('applicant_contact')
        interest = data.get('interest')
        published = data.get('published')
        pub_date = data.get('pub_date')
        pub_country = data.get('pub_country')
        author_name = data.get('author_name')
        author_address = data.get('author_address')
        author_nationality = data.get('author_nationality')
        author_deceased = data.get('author_deceased')
        declaration_date = data.get('declaration_date')
        declaration_place = data.get('declaration_place')
        submit_date = data.get('submit_date')

        logger.debug(f"Received: {id_proof}, {type_of_work}, {title}, {language}, {applicant_name}, {applicant_address}, {applicant_nationality}, {applicant_contact}, {interest}, {published}, {pub_date}, {pub_country}, {author_name}, {author_address}, {author_nationality}, {author_deceased}, {declaration_date}, {declaration_place}, {submit_date}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO copyright_registration (id_proof, type_of_work, title, language, applicant_name, applicant_address, applicant_nationality, applicant_contact, interest, published, pub_date, pub_country, author_name, author_address, author_nationality, author_deceased, declaration_date, declaration_place, submit_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, type_of_work, title, language, applicant_name, applicant_address, applicant_nationality, applicant_contact, interest, published, pub_date, pub_country, author_name, author_address, author_nationality, author_deceased, declaration_date, declaration_place, submit_date))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Copyright registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /copyright-registration")
        return f"Internal Server Error: {e}", 500

@app.route("/submit-patent-application", methods=['GET'])
def patent_form():
    return render_template('../html/patent.html')

@app.route('/submit-patent-application', methods=['POST'])
def submit_patent_application():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        applicant_name = data.get('applicant_name')
        applicant_nationality = data.get('applicant_nationality')
        applicant_address = data.get('applicant_address')
        applicant_contact = data.get('applicant_contact')
        applicant_email = data.get('applicant_email')
        category = data.get('category')
        inventor1_name = data.get('inventor1_name')
        inventor1_nationality = data.get('inventor1_nationality')
        inventor1_address = data.get('inventor1_address')
        inventor2_name = data.get('inventor2_name')
        inventor2_nationality = data.get('inventor2_nationality')
        inventor2_address = data.get('inventor2_address')
        title = data.get('title')
        application_type = data.get('application_type')
        statement = data.get('statement')
        inventor1_signature = data.get('inventor1_signature')
        inventor2_signature = data.get('inventor2_signature')
        attachments = data.get('attachments')
        applicant_sign_name = data.get('applicant_sign_name')
        place = data.get('place')
        date = data.get('date')
        signature = data.get('signature')

        logger.debug(f"Received: {id_proof}, {applicant_name}, {applicant_nationality}, {applicant_address}, {applicant_contact}, {applicant_email}, {category}, {inventor1_name}, {inventor1_nationality}, {inventor1_address}, {inventor2_name}, {inventor2_nationality}, {inventor2_address}, {title}, {application_type}, {statement}, {inventor1_signature}, {inventor2_signature}, {attachments}, {applicant_sign_name}, {place}, {date}, {signature}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO patent_applications (id_proof, applicant_name, applicant_nationality, applicant_address, applicant_contact, applicant_email, category, inventor1_name, inventor1_nationality, inventor1_address, inventor2_name, inventor2_nationality, inventor2_address, title, application_type, statement, inventor1_signature, inventor2_signature, attachments, applicant_sign_name, place, date, signature) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, applicant_name, applicant_nationality, applicant_address, applicant_contact, applicant_email, category, inventor1_name, inventor1_nationality, inventor1_address, inventor2_name, inventor2_nationality, inventor2_address, title, application_type, statement, inventor1_signature, inventor2_signature, attachments, applicant_sign_name, place, date, signature))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Patent application submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /submit-patent-application")
        return f"Internal Server Error: {e}", 500

@app.route('/startup-registration')
def startup_form():
    return render_template('../html/start.html')

@app.route('/startup-registration', methods=['POST'])
def submit_startup_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        entity_name = data.get("entity_name")
        entity_type = data.get("entity_type")
        reg_number = data.get("registration_number")
        reg_date = data.get("registration_date")
        cin = data.get("cin")
        pan = data.get("pan")
        website = data.get("website")
        address = data.get("address")
        city = data.get("city")
        state = data.get("state")
        pin = data.get("pin")
        phone = data.get("phone")
        email = data.get("email")
        founder_name = data.get("founder_name")
        founder_role = data.get("founder_role")
        founder_mobile = data.get("founder_mobile")
        founder_email = data.get("founder_email")
        description = data.get("description")
        innovation_type = data.get("innovation_type")
        scalability = data.get("scalability")
        funding_received = data.get("funding_received")
        invester_name = data.get("invester_name")
        funding_amount = data.get("funding_amount")
        funding_date = data.get("funding_date")
        submit_date = data.get("submit_date")

        logger.debug(f"Received: {id_proof}, {entity_name}, {entity_type}, {reg_number}, {reg_date}, {cin}, {pan}, {website}, {address}, {city}, {state}, {pin}, {phone}, {email}, {founder_name}, {founder_role}, {founder_mobile}, {founder_email}, {description}, {innovation_type}, {scalability}, {funding_received}, {invester_name}, {funding_amount}, {funding_date}, {submit_date}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO startup_registrations (id_proof, entity_name, entity_type, reg_number, reg_date, cin, pan, website, address, city, state, pin, phone, email, founder_name, founder_role, founder_mobile, founder_email, description, innovation_type, scalability, funding_received, invester_name, funding_amount, funding_date, submit_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, entity_name, entity_type, reg_number, reg_date, cin, pan, website, address, city, state, pin, phone, email, founder_name, founder_role, founder_mobile, founder_email, description, innovation_type, scalability, funding_received, invester_name, funding_amount, funding_date, submit_date))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Startup registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /startup-registration")
        return f"Internal Server Error: {e}", 500

@app.route('/llc-registration')
def llc_form():
    return render_template('../html/llc.html')

@app.route('/llc-registration', methods=['POST'])
def submit_llc_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        company_name = data.get('company_name')
        buisness_address = data.get('buisness_address')
        mailing_address = data.get('mailing_address')
        agent_name = data.get('agent_name')
        agent_address = data.get('agent_address')
        buisness_phone = data.get('buisness_phone')
        duration = data.get('duration')
        submit_date = data.get('submit_date')
        owner_name = data.get('owner_name')
        owner_address = data.get('owner_address')
        owner_email = data.get('owner_email')
        owner_role = data.get('owner_role')
        manager_name = data.get('manager_name')
        manager_address = data.get('manager_address')
        option = data.get('option')
        organization_type = data.get('organization_type')
        signature = data.get('signature')
        submit_date = data.get('submit_date')

        logger.debug(f"Received: {id_proof}, {company_name}, {buisness_address}, {mailing_address}, {agent_name}, {agent_address}, {buisness_phone}, {duration}, {submit_date}, {owner_name}, {owner_address}, {owner_email}, {owner_role}, {manager_name}, {manager_address}, {option}, {organization_type}, {signature}, {submit_date}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO llc_registrations (id_proof, company_name, buisness_address, mailing_address, agent_name, agent_address, buisness_phone, duration, submit_date, owner_name, owner_address, owner_email, owner_role, manager_name, manager_address, option, organization_type, signature, submit_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, company_name, buisness_address, mailing_address, agent_name, agent_address, buisness_phone, duration, submit_date, owner_name, owner_address, owner_email, owner_role, manager_name, manager_address, option, organization_type, signature, submit_date))    
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'LLC registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /llc-registration")
        return f"Internal Server Error: {e}", 500
    

@app.route('/company-registration')
def company_registration():
    return render_template('../html/uk.html')

@app.route('/company-registration', methods=['POST'])
def submit_company_registration():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        proposed_name = data.get('proposed_name')
        company_type = data.get('company_type')
        registered_office_address = data.get('registered_office_address')
        office_location = data.get('office_location')
        director_name = data.get('director_name')
        dob = data.get('dob')
        nationality = data.get('nationality')
        occupation = data.get('occupation')
        service_address = data.get('service_address')
        residential_address = data.get('residential_address')
        secretary_name = data.get('secretary_name')
        secretary_address = data.get('secretary_address')
        total_shares = data.get('total_shares')
        share_value = data.get('share_value')
        currency = data.get('currency')
        shareholder_1 = data.get('shareholder_1')
        shareholder_2 = data.get('shareholder_2')
        signature = data.get('signature')
        submission_date = data.get('submission_date')

        logger.debug(f"Received: {id_proof}, {proposed_name}, {company_type}, {registered_office_address}, {office_location}, {director_name}, {dob}, {nationality}, {occupation}, {service_address}, {residential_address}, {secretary_name}, {secretary_address}, {total_shares}, {share_value}, {currency}, {shareholder_1}, {shareholder_2}, {signature}, {submission_date}")
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO uk_registration (
                id_proof, proposed_name, company_type, registered_office_address,
                office_location, director_name, dob, nationality, occupation,
                service_address, residential_address, secretary_name, secretary_address,
                total_shares, share_value, currency, shareholder_1, shareholder_2,
                signature, submission_date
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            id_proof, proposed_name, company_type, registered_office_address,
            office_location, director_name, dob, nationality, occupation,
            service_address, residential_address, secretary_name, secretary_address,
            total_shares, share_value, currency, shareholder_1, shareholder_2,
            signature, submission_date
        ))
        conn.commit()
        cursor.close()
        conn.close()

        return jsonify({'message': 'Company registration submitted successfully'}), 201

    except Exception as e:
        logger.exception("Error in /company-registration")
        return jsonify({"error": str(e)}), 500




@app.route('/china-registration')
def china_registration_form():
    return render_template('../html/china.html')

@app.route('/china-registration', methods=['POST'])
def submit_china_registration():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        company_name_chinese = data.get('company_name_chinese')
        alternate_name = data.get('alternate_name')
        company_type = data.get('company_type')
        registered_address = data.get('registered_address')
        business_scope = data.get('business_scope')
        capital_rmb = data.get('capital_rmb')
        operating_term = data.get('operating_term')
        investor_name = data.get('investor_name')
        investor_nationality = data.get('investor_nationality')
        investor_id = data.get('investor_id')
        investor_address = data.get('investor_address')
        ownership_percent = data.get('ownership_percent')
        legal_rep_name = data.get('legal_rep_name')
        legal_rep_nationality = data.get('legal_rep_nationality')
        legal_rep_id = data.get('legal_rep_id')
        legal_rep_position = data.get('legal_rep_position')
        supervisor_name = data.get('supervisor_name')
        supervisor_contact = data.get('supervisor_contact')
        executive_director = data.get('executive_director')
        finance_manager = data.get('finance_manager')
        contact_person_china = data.get('contact_person_china')
        submitted_at = data.get('submitted_at')

        logger.debug(f"Received: {id_proof}, {company_name_chinese}, {alternate_name}, {company_type}, {registered_address}, {business_scope}, {capital_rmb}, {operating_term}, {investor_name}, {investor_nationality}, {investor_id}, {investor_address}, {ownership_percent}, {legal_rep_name}, {legal_rep_nationality}, {legal_rep_id}, {legal_rep_position}, {supervisor_name}, {supervisor_contact}, {executive_director}, {finance_manager}, {contact_person_china}, {submitted_at}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO china_registration (id_proof, company_name_chinese, alternate_name, company_type, registered_address, business_scope, capital_rmb, operating_term, investor_name, investor_nationality, investor_id, investor_address, ownership_percent, legal_rep_name, legal_rep_nationality, legal_rep_id, legal_rep_position, supervisor_name, supervisor_contact, executive_director, finance_manager, contact_person_china, submitted_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, company_name_chinese, alternate_name, company_type, registered_address, business_scope, capital_rmb, operating_term, investor_name, investor_nationality, investor_id, investor_address, ownership_percent, legal_rep_name, legal_rep_nationality, legal_rep_id, legal_rep_position, supervisor_name, supervisor_contact, executive_director, finance_manager, contact_person_china, submitted_at))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'China registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /china-registration")
        return f"Internal Server Error: {e}", 500
    
@app.route('/web-service-form')
def web_service_form():
    return render_template('../html/web.html')

@app.route('/web-service-form', methods=['POST'])
def submit_web_service_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        full_name = data.get('full_name')
        company_name = data.get('company_name')
        email = data.get('email')
        phone = data.get('phone')
        address = data.get('address')
        services = data.get('services') 
        project_description = data.get('project_description')
        target_audience = data.get('target_audience')
        existing_website = data.get('existing_website')
        website_url = data.get('website_url')
        preferred_technology = data.get('preferred_technology')
        content_availability = data.get('content_availability')
        example_websites = data.get('example_websites')
        color_scheme = data.get('color_scheme')
        start_date = data.get('start_date')
        deadline = data.get('deadline')
        budget_range = data.get('budget_range')
        notes = data.get('notes')
        signature = data.get('signature')
        form_date = data.get('form_date')

        logger.debug(f"Received: {id_proof}, {full_name}, {company_name}, {email}, {phone}, {address}, {services}, {project_description}, {target_audience}, {existing_website}, {website_url}, {preferred_technology}, {content_availability}, {example_websites}, {color_scheme}, {start_date}, {deadline}, {budget_range}, {notes}, {signature}, {form_date}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO web_service_form (id_proof, full_name, company_name, email, phone, address, services, project_description, target_audience, existing_website, website_url, preferred_technology, content_availability, example_websites, color_scheme, start_date, deadline, budget_range, notes, signature, form_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, full_name, company_name, email, phone, address, services, project_description, target_audience, existing_website, website_url, preferred_technology, content_availability, example_websites, color_scheme, start_date, deadline, budget_range, notes, signature, form_date))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Web service form submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /web-service-form")
        return f"Internal Server Error: {e}", 500
    
@app.route('/proprietor-registration')
def proprietor_form():
    return render_template('../html/proprietor.html')

@app.route('/proprietor-registration', methods=['POST'])
def submit_proprietor_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        full_name = data.get('full_name')
        parent_name = data.get('parent_name')
        dob = data.get('dob')
        gender = data.get('gender')
        aadhaar = data.get('aadhaar')
        pan = data.get('pan')
        mobile = data.get('mobile')
        email = data.get('email')
        res_address = data.get('res_address')
        res_pin = data.get('res_pin')
        firm_name = data.get('firm_name')
        business_type = data.get('business_type')
        nature = data.get('nature')
        business_address = data.get('business_address')
        business_city = data.get('business_city')
        business_pin = data.get('business_pin')
        commencement_date = data.get('commencement_date')
        website = data.get('website')
        bank_name = data.get('bank_name')
        account_type = data.get('account_type')
        ifsc = data.get('ifsc')
        branch_address = data.get('branch_address')
        registrations = data.get('registrations')
        place = data.get('place')
        declaration_date = data.get('declaration_date')
        submitted_at = data.get('submitted_at')

        logger.debug(f"Received: {id_proof}, {full_name}, {parent_name}, {dob}, {gender}, {aadhaar}, {pan}, {mobile}, {email}, {res_address}, {res_pin}, {firm_name}, {business_type}, {nature}, {business_address}, {business_city}, {business_pin}, {commencement_date}, {website}, {bank_name}, {account_type}, {ifsc}, {branch_address}, {registrations}, {place}, {declaration_date}, {submitted_at}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO proprietor_registration (id_proof, full_name, parent_name, dob, gender, aadhaar, pan, mobile, email, res_address, res_pin, firm_name, business_type, nature, business_address, business_city, business_pin, commencement_date, website, bank_name, account_type, ifsc, branch_address, registrations, place, declaration_date, submitted_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, full_name, parent_name, dob, gender, aadhaar, pan, mobile, email, res_address, res_pin, firm_name, business_type, nature, business_address, business_city, business_pin, commencement_date, website, bank_name, account_type, ifsc, branch_address, registrations, place, declaration_date, submitted_at))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Proprietor registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /proprietor-registration")
        return f"Internal Server Error: {e}", 500
    

@app.route('/partnership-form')
def partnership_form():
    return render_template('../html/partnership.html')

@app.route('/partnership-form', methods=['POST'])
def submit_partnership_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        firm_name = data.get('firm_name')
        business_nature = data.get('business_nature')
        address = data.get('address')
        city = data.get('city')
        state = data.get('state')
        pincode = data.get('pincode')
        phone = data.get('phone')
        email = data.get('email')
        commencement_date = data.get('commencement_date')
        duration_type = data.get('duration_type')
        duration_from = data.get('duration_from')
        duration_to = data.get('duration_to')

        partner_names = data.get('partner_names', [])
        father_names = data.get('father_names', [])
        partner_addresses = data.get('partner_addresses', [])
        ages = data.get('ages', [])
        pans = data.get('pans', [])
        shares = data.get('shares', [])
        capital_names = data.get('capital_names', [])
        contributions = data.get('contributions', [])

        bank_name = data.get('bank_name')
        branch = data.get('branch')
        account_number = data.get('account_number')
        signature = data.get('signature')
        submitted_at = data.get('submitted_at')
        logger.debug(f"Received: {id_proof}, {firm_name}, {business_nature}, {address}, {city}, {state}, {pincode}, {phone}, {email}, {commencement_date}, {duration_type}, {duration_from}, {duration_to}, {partner_names}, {father_names}, {partner_addresses}, {ages}, {pans}, {shares}, {capital_names}, {contributions}, {bank_name}, {branch}, {account_number}, {signature}, {submitted_at}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO partnership_registration (id_proof, firm_name, business_nature, address, city, state, pincode, phone, email, commencement_date, duration_type, duration_from, duration_to, partner_names, father_names, partner_addresses, ages, pans, shares, capital_names, contributions, bank_name, branch, account_number, signature, submitted_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, firm_name, business_nature, address, city, state, pincode, phone, email, commencement_date, duration_type, duration_from, duration_to, partner_names, father_names, partner_addresses, ages, pans, shares, capital_names, contributions, bank_name, branch, account_number, signature, submitted_at))
        
        for i in range(len(partner_names)):
            cursor.execute("""
            INSERT INTO partnership_partners (firm_name, partner_name, father_name, address, age, pan, share) VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                        (firm_name, partner_names[i], father_names[i], partner_addresses[i], ages[i], pans[i], shares[i]))
            conn.commit()
        for i in range(len(capital_names)):
            cursor.execute("""
                           INSERT INTO partnership_capital (firm_name, capital_partner_name, capital_contribution) VALUES (%s, %s, %s)""",
                            (firm_name, capital_names[i], contributions[i]))
            conn.commit()
            cursor.close()
            conn.close()
            return jsonify({'message': 'Partnership registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /partnership-form")
        return f"Internal Server Error: {e}", 500

@app.route('/opc-form')
def opc_form():
    return render_template('../html/opc.html')

@app.route('/opc-form', methods=['POST'])
def submit_opc_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        company_name = data.get('company_name')
        state = data.get('state')
        auth_capital = data.get('auth_capital')
        paid_capital = data.get('paid_capital')
        main_activity = data.get('main_activity')
        full_name = data.get('full_name')
        father_name = data.get('father_name')
        dob = data.get('dob')
        nationality = data.get('nationality')
        pan = data.get('pan')
        aadhaar = data.get('aadhaar')
        din = data.get('din')
        mobile = data.get('mobile')
        email = data.get('email')
        res_address = data.get('res_address')
        occupation = data.get('occupation')
        nominee_name = data.get('nominee_name')
        nominee_father = data.get('nominee_father')
        nominee_dob = data.get('nominee_dob')
        nominee_pan = data.get('nominee_pan')
        nominee_aadhaar = data.get('nominee_aadhaar')
        nominee_address = data.get('nominee_address')
        nominee_relation = data.get('nominee_relation')
        office_address = data.get('office_address')
        office_city = data.get('office_city')
        office_state = data.get('office_state')
        office_pin = data.get('office_pin')
        office_email = data.get('office_email')
        office_phone = data.get('office_phone')
        declarant_name = data.get('declarant_name')
        declaration_date = data.get('declaration_date')

        logger.debug(f"Received: {id_proof}, {company_name}, {state}, {auth_capital}, {paid_capital}, {main_activity}, {full_name}, {father_name}, {dob}, {nationality}, {pan}, {aadhaar}, {din}, {mobile}, {email}, {res_address}, {occupation}, {nominee_name}, {nominee_father}, {nominee_dob}, {nominee_pan}, {nominee_aadhaar}, {nominee_address}, {nominee_relation}, {office_address}, {office_city}, {office_state}, {office_pin}, {office_email}, {office_phone}, {declarant_name}, {declaration_date}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO opc_registration (id_proof, company_name, state, auth_capital, paid_capital, main_activity, full_name, father_name, dob, nationality, pan, aadhaar, din, mobile, email, res_address, occupation, nominee_name, nominee_father, nominee_dob, nominee_pan, nominee_aadhaar, nominee_address, nominee_relation, office_address, office_city, office_state, office_pin, office_email, office_phone, declarant_name, declaration_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, company_name, state, auth_capital, paid_capital, main_activity, full_name, father_name, dob, nationality, pan, aadhaar, din, mobile, email, res_address, occupation, nominee_name, nominee_father, nominee_dob, nominee_pan, nominee_aadhaar, nominee_address, nominee_relation, office_address, office_city, office_state, office_pin, office_email, office_phone, declarant_name, declaration_date))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'OPC registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /opc-form")
        return f"Internal Server Error: {e}", 500
    

@app.route('/private-company-registration')
def private_company_registration():
    return render_template('../html/private.html')

@app.route('/private-company-registration', methods=['POST'])
def submit_private_company_registration():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        proposed_name = data.get('proposed_name')
        business_activity = data.get('business_activity')
        nic_code = data.get('nic_code')
        objectives = data.get('objectives')
        registered_office = data.get('registered_office')
        email = data.get('email')
        mobile = data.get('mobile') 
        authorized_capital = data.get('authorized_capital')
        paidup_capital = data.get('paidup_capital')
        director_name = data.get('director_name')
        director_din = data.get('director_din')
        director_address = data.get('director_address')
        director_nationality = data.get('director_nationality')
        director_role = data.get('director_role')

        logger.debug(f"Received: {id_proof}, {proposed_name}, {business_activity}, {nic_code}, {objectives}, {registered_office}, {email}, {mobile}, {authorized_capital}, {paidup_capital}, {director_name}, {director_din}, {director_address}, {director_nationality}, {director_role}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO private_company_registration (id_proof, proposed_name, business_activity, nic_code, objectives, registered_office, email, mobile, authorized_capital, paidup_capital, director_name, director_din, director_address, director_nationality, director_role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, proposed_name, business_activity, nic_code, objectives, registered_office, email, mobile, authorized_capital, paidup_capital, director_name, director_din, director_address, director_nationality, director_role))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Private company registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /private-company-registration")
        return f"Internal Server Error: {e}", 500
    
@app.route('/llp-registration')
def llp_form():
    return render_template('../html/llp.html')

@app.route('/llp-registration', methods=['POST'])
def submit_llp_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        name = data.get('llp_name')
        nic_main = data.get('nic_main')
        nic_desc = data.get('nic_desc')
        address_line = data.get('address_line')
        city = data.get('city')
        state = data.get('state')
        pincode = data.get('pincode')
        email = data.get('email')
        mobile = data.get('mobile')
        
        partner1 = {
        "name": data.get('p1_name'),
        "din": data.get('p1_din'),
        "pan": data.get('p1_pan'),
        "aadhaar": data.get('p1_aadhaar'),
        "address": data.get('p1_address'),
        "email": data.get('p1_email'),
        "mobile": data.get('p1_mobile'),
        "nationality": data.get('p1_nationality'),
        "occupation": data.get('p1_occupation'),
        "capital": data.get('p1_capital')
        }

        partner2 = {
        "name": data.get('p2_name'),
        "din": data.get('p2_din'),
        "pan": data.get('p2_pan'),
        "aadhaar": data.get('p2_aadhaar'),
        "address": data.get('p2_address'),
        "email": data.get('p2_email'),
        "mobile": data.get('p2_mobile'),
        "nationality": data.get('p2_nationality'),
        "occupation": data.get('p2_occupation'),
        "capital": data.get('p2_capital')
        }

        total_capital = data.get('total_capital')

        logger.debug(f"Received: {id_proof}, {name}, {nic_main}, {nic_desc}, {address_line}, {city}, {state}, {pincode}, {email}, {mobile}, {partner1}, {partner2}, {total_capital}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO llp_registrations (
                       name, nic_main, nic_desc, address_line, city, state, pincode,
                       email, mobile, partner1_name, partner1_din, partner1_pan, partner1_aadhaar,
                       partner1_address, partner1_email, partner1_mobile, partner1_nationality, partner1_occupation,
                       partner2_name, partner2_din, partner2_pan, partner2_aadhaar, partner2_address,
                       partner2_email, partner2_mobile, partner2_nationality, partner2_occupation,
                       total_capital, partner1_capital, partner2_capital
                       ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                       %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                       """, (
                           name, nic_main, nic_desc, address_line, city, state, pincode,
                           email, mobile, partner1["name"], partner1["din"], partner1["pan"], partner1["aadhaar"],
                           partner1["address"], partner1["email"], partner1["mobile"], partner1["nationality"], partner1["occupation"],
                           partner2["name"], partner2["din"], partner2["pan"], partner2["aadhaar"], partner2["address"],
                           partner2["email"], partner2["mobile"], partner2["nationality"], partner2["occupation"],
                           total_capital, partner1["capital"], partner2["capital"]
                           ))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "LLP Registration submitted successfully!"})
    except Exception as e:
        logger.exception("Error in /llp-registration")
        return f"Internal Server Error: {e}", 500
    
@app.route('/public-limited-registration')
def public_limited_form():
    return render_template('../html/public.html')

@app.route('/public-limited-registration', methods=['POST'])
def submit_public_limited_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        company_name_1 = data.get('company_name_1')
        company_name_2 = data.get('company_name_2')
        business_activity = data.get('business_activity')
        authorized_capital = data.get('authorized_capital')
        paidup_capital = data.get('paidup_capital')
        address = data.get('address')
        city = data.get('city')
        state = data.get('state')
        pin = data.get('pin')
        email = data.get('email')
        phone = data.get('phone')
        main_object = data.get('main_object')
        date = data.get('date')
        place = data.get('place')
        applicant_name = data.get('applicant_name')
        signature = data.get('signature')
        
        logger.debug(f"Received: {id_proof}, {company_name_1}, {company_name_2}, {business_activity}, {authorized_capital}, {paidup_capital}, {address}, {city}, {state}, {pin}, {email}, {phone}, {main_object}, {date}, {place}, {applicant_name}, {signature}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO public_limited_companies (id_proof, company_name_1, company_name_2, business_activity, authorized_capital, paidup_capital, address, city, state, pin, email, phone, main_object, date, place, applicant_name, signature) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, company_name_1, company_name_2, business_activity, authorized_capital, paidup_capital, address, city, state, pin, email, phone, main_object, date, place, applicant_name, signature))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Public limited company registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /public-limited-registration")
        return f"Internal Server Error: {e}", 500
    
@app.route('/sec8-company-registration')
def sec8_company_registration():
    return render_template('../html/sec8.html')

@app.route('/sec8-company-registration', methods=['POST'])
def submit_sec8_company_registration():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        name_pref_1 = data.get('name_pref_1')
        name_pref_2 = data.get('name_pref_2')
        objectives = data.get('objectives')
        nature_of_work = data.get('nature_of_work')
        reg_address = data.get('reg_address')
        reg_city = data.get('reg_city')
        reg_state = data.get('reg_state')
        reg_pincode = data.get('reg_pincode')
        reg_email = data.get('reg_email')
        reg_phone = data.get('reg_phone')
        directors = data.get('directors')
        authorized_capital = data.get('authorized_capital')
        paid_up_capital = data.get('paid_up_capital')

        logger.debug(f"Received: {id_proof}, {name_pref_1}, {name_pref_2}, {objectives}, {nature_of_work}, {reg_address}, {reg_city}, {reg_state}, {reg_pincode}, {reg_email}, {reg_phone}, {directors}, {authorized_capital}, {paid_up_capital}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO sec8_registration (id_proof, name_pref_1, name_pref_2, objectives, nature_of_work, reg_address, reg_city, reg_state, reg_pincode, reg_email, reg_phone, directors, authorized_capital, paid_up_capital) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, name_pref_1, name_pref_2, objectives, nature_of_work, reg_address, reg_city, reg_state, reg_pincode, reg_email, reg_phone, directors, authorized_capital, paid_up_capital))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'SEC 8 company registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /sec8-company-registration")
        return f"Internal Server Error: {e}", 500
    
@app.route('/name-registration')
def name_registration():
    return render_template('../html/n.html')

@app.route('/name-registration', methods=['POST'])
def submit_name_registration():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        current_name = data.get('current_name')
        cin = data.get('cin')
        company_type = data.get('company_type')
        incorporation_date = data.get('incorporation_date')
        registered_address = data.get('registered_address')
        proposed_name = data.get('proposed_name')
        name_srn = data.get('name_srn') 
        reason = data.get('reason')
        board_meeting_date = data.get('board_meeting_date')
        resolution_date = data.get('resolution_date')
        director_name = data.get('director_name')
        director_din = data.get('director_din')
        submission_date = data.get('submission_date')

        logger.debug(f"Received: {id_proof}, {current_name}, {cin}, {company_type}, {incorporation_date}, {registered_address}, {proposed_name}, {name_srn}, {reason}, {board_meeting_date}, {resolution_date}, {director_name}, {director_din}, {submission_date}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO company_name_changes (id_proof, current_name, cin, company_type, incorporation_date, registered_address, proposed_name, name_srn, reason, board_meeting_date, resolution_date, director_name, director_din, submission_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, current_name, cin, company_type, incorporation_date, registered_address, proposed_name, name_srn, reason, board_meeting_date, resolution_date, director_name, director_din, submission_date))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Name registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /name-registration")
        return f"Internal Server Error: {e}", 500

@app.route('/director-appointment')
def director_form():
    return render_template('../html/addition.html')

@app.route('/director-appointment', methods=['POST'])
def submit_director_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        company_name = data.get('company_name')
        cin = data.get('cin')
        reg_office = data.get('reg_office')
        company_email = data.get('company_email')
        full_name = data.get('full_name')
        father_name = data.get('father_name')
        din = data.get('din')
        dob = data.get('dob')
        nationality = data.get('nationality')
        address = data.get('address')
        email = data.get('email')
        mobile = data.get('mobile')
        occupation = data.get('occupation')
        category = data.get('category')
        appointment_date = data.get('appointment_date')
        designation = data.get('designation')
        consent_received = data.get('consent_received')
        
        logger.debug(f"Received: {id_proof}, {company_name}, {cin}, {reg_office}, {company_email}, {full_name}, {father_name}, {din}, {dob}, {nationality}, {address}, {email}, {mobile}, {occupation}, {category}, {appointment_date}, {designation}, {consent_received}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO director_appointments (id_proof, company_name, cin, reg_office, company_email, full_name, father_name, din, dob, nationality, address, email, mobile, occupation, category, appointment_date, designation, consent_received) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, company_name, cin, reg_office, company_email, full_name, father_name, din, dob, nationality, address, email, mobile, occupation, category, appointment_date, designation, consent_received))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Director appointment submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /director-appointment")
        return f"Internal Server Error: {e}", 500
    
@app.route("/address-change-form")
def address_change_form():
    return render_template("address_change_form.html")

@app.route("/submit-address-change", methods=["POST"])
def submit_address_change():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof') 
        full_name = request.form["full_name"]
        customer_id = request.form["customer_id"]
        phone = request.form["phone"]
        email = request.form["email"]
        old_address = request.form["old_address"]
        old_city = request.form["old_city"]
        old_state = request.form["old_state"]
        old_pincode = request.form["old_pincode"]
        new_address = request.form["new_address"]
        new_city = request.form["new_city"]
        new_state = request.form["new_state"]
        new_pincode = request.form["new_pincode"]
        effective_type = request.form["effective_date_type"]
        scheduled_date = request.form.get("scheduled_date", None)
        signature = request.form["signature"]
        place = request.form["place"]
        form_date = request.form["form_date"]

        logger.debug(f"Received: {id_proof}, {full_name}, {customer_id}, {phone}, {email}, {old_address}, {old_city}, {old_state}, {old_pincode}, {new_address}, {new_city}, {new_state}, {new_pincode}, {effective_type}, {scheduled_date}, {signature}, {place}, {form_date}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO address_change_requests (id_proof, full_name, customer_id, phone, email, old_address, old_city, old_state, old_pincode, new_address, new_city, new_state, new_pincode, effective_type, scheduled_date, signature, place, form_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, full_name, customer_id, phone, email, old_address, old_city, old_state, old_pincode, new_address, new_city, new_state, new_pincode, effective_type, scheduled_date, signature, place, form_date))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Address change request submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /address-change-form")
        return f"Internal Server Error: {e}", 500
    
@app.route('/company-winding-up')
def winding_up_form():
    return render_template('../html/winding.html')

@app.route('/company-winding-up', methods=['POST'])
def submit_winding_up_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        company_name = data.get('company_name')
        cin = data.get('cin')
        registered_address = data.get('registered_address')
        incorporation_date = data.get('incorporation_date')
        authorized_capital = data.get('authorized_capital')
        paid_up_capital = data.get('paid_up_capital')
        mode = data.get('mode')
        reason = data.get('reason')
        board_resolution = data.get('board_resolution')
        special_resolution = data.get('special_resolution')
        declaration = data.get('declaration')
        director1 = data.get('director1')
        director2 = data.get('director2')
        declaration_date = data.get('declaration_date')

        logger.debug(f"Received: {id_proof}, {company_name}, {cin}, {registered_address}, {incorporation_date}, {authorized_capital}, {paid_up_capital}, {mode}, {reason}, {board_resolution}, {special_resolution}, {declaration}, {director1}, {director2}, {declaration_date}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO company_winding_up (id_proof, company_name, cin, registered_address, incorporation_date, authorized_capital, paid_up_capital, mode, reason, board_resolution, special_resolution, declaration, director1, director2, declaration_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, company_name, cin, registered_address, incorporation_date, authorized_capital, paid_up_capital, mode, reason, board_resolution, special_resolution, declaration, director1, director2, declaration_date))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Company winding up submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /company-winding-up")
        return f"Internal Server Error: {e}", 500
    
@app.route('/company-strikeoff')
def strikeoff_form():
    return render_template('../html/pvt.html')

@app.route('/company-strikeoff', methods=['POST'])
def submit_strikeoff_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        cin = data.get('cin')
        company_name = data.get('company_name')
        address = data.get('address')
        email = data.get('email')
        authorized_name = data.get('authorized_name')
        designation = data.get('designation')
        din = data.get('din')
        contact = data.get('contact')
        reason = data.get('reason')
        other_reason = data.get('other_reason')
        signature = data.get('signature')
        declaration_date = data.get('declaration_date')
        declaration_din = data.get('declaration_din')

        logger.debug(f"Received: {id_proof}, {cin}, {company_name}, {address}, {email}, {authorized_name}, {designation}, {din}, {contact}, {reason}, {other_reason}, {signature}, {declaration_date}, {declaration_din}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO company_strikeoff (id_proof, cin, company_name, address, email, authorized_name, designation, din, contact, reason, other_reason, signature, declaration_date, declaration_din) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, cin, company_name, address, email, authorized_name, designation, din, contact, reason, other_reason, signature, declaration_date, declaration_din))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Company strikeoff submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /company-strikeoff")
        return f"Internal Server Error: {e}", 500

@app.route('/din-surrender')
def din_surrender_form():
    return render_template('../html/din.html')

@app.route('/din-surrender', methods=['POST'])
def submit_din_surrender_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        din = data.get('din')
        reason = data.get('reason')
        full_name = data.get('full_name')
        father_name = data.get('father_name')
        dob = data.get('dob')
        gender = data.get('gender')
        nationality = data.get('nationality')
        pan = data.get('pan')
        passport_no = data.get('passport_no')
        address = data.get('address')
        email = data.get('email')
        mobile = data.get('mobile')

        logger.debug(f"Received: {id_proof}, {din}, {reason}, {full_name}, {father_name}, {dob}, {gender}, {nationality}, {pan}, {passport_no}, {address}, {email}, {mobile}")  
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO din_surrender (id_proof, din, reason, full_name, father_name, dob, gender, nationality, pan, passport_no, address, email, mobile) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, din, reason, full_name, father_name, dob, gender, nationality, pan, passport_no, address, email, mobile))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'DIN surrender submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /din-surrender")
        return f"Internal Server Error: {e}", 500

@app.route("/trade-license-registration")
def trade_license_form():
    return render_template("../html/license.html")

@app.route("/trade-license-registration", methods=["POST"])
def submit_trade_license_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        applicant_name = data.get('applicant_name')
        father_or_spouse = data.get('father_or_spouse')
        res_address = data.get('res_address')
        mobile = data.get('mobile')
        email = data.get('email')
        business_type = data.get('business_type')
        business_name = data.get('business_name')
        business_address = data.get('business_address')
        premises = data.get('premises')
        ward = data.get('ward')
        commencement_date = data.get('commencement_date')
        employees = data.get('employees')
        trade_classification = data.get('trade_classification')
        place = data.get('place')

        logger.debug(f"Received: {id_proof}, {applicant_name}, {father_or_spouse}, {res_address}, {mobile}, {email}, {business_type}, {business_name}, {business_address}, {premises}, {ward}, {commencement_date}, {employees}, {trade_classification}, {place}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO trade_license (id_proof, applicant_name, father_or_spouse, res_address, mobile, email, business_type, business_name, business_address, premises, ward, commencement_date, employees, trade_classification, place) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, applicant_name, father_or_spouse, res_address, mobile, email, business_type, business_name, business_address, premises, ward, commencement_date, employees, trade_classification, place))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Trade license submitted successfully'}), 201
    except Exception as e:  
        logger.exception("Error in /trade-license-registration")
        return f"Internal Server Error: {e}", 500
    
@app.route('/fssai-registration')
def fssai_form():
    return render_template('../html/fssai.html')

@app.route('/fssai-registration', methods=['POST'])
def submit_fssai_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        business_name = data.get('business_name')
        constitution_type = data.get('constitution_type')
        nature_of_business = data.get('nature_of_business')
        annual_turnover = data.get('annual_turnover')
        building = data.get('building')
        city = data.get('city')
        state = data.get('state')
        pincode = data.get('pincode')
        contact = data.get('contact')
        email = data.get('email')
        food_category = data.get('food_category')
        proprietor_name = data.get('proprietor_name')
        designation = data.get('designation')
        mobile = data.get('mobile')
        proprietor_email = data.get('proprietor_email')
        proprietor_address = data.get('proprietor_address')
        declaration_name = data.get('declaration_name')
        declaration_place = data.get('declaration_place')
        declaration_date = data.get('declaration_date')

        logger.debug(f"Received: {id_proof}, {business_name}, {constitution_type}, {nature_of_business}, {annual_turnover}, {building}, {city}, {state}, {pincode}, {contact}, {email}, {food_category}, {proprietor_name}, {designation}, {mobile}, {proprietor_email}, {proprietor_address}, {declaration_name}, {declaration_place}, {declaration_date}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO fssai_registrations (id_proof, business_name, constitution_type, nature_of_business, annual_turnover, building, city, state, pincode, contact, email, food_category, proprietor_name, designation, mobile, proprietor_email, proprietor_address, declaration_name, declaration_place, declaration_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, business_name, constitution_type, nature_of_business, annual_turnover, building, city, state, pincode, contact, email, food_category, proprietor_name, designation, mobile, proprietor_email, proprietor_address, declaration_name, declaration_place, declaration_date))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'FSSAI registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /fssai-registration")
        return f"Internal Server Error: {e}", 500

@app.route("/shop-establishment")
def shop_form():
    return render_template("../html/shop.html")

@app.route("/shop-establishment", methods=["POST"])
def submit_shop_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        full_name = data.get('full_name')
        father_or_husband = data.get('father_or_husband')
        res_address = data.get('res_address')
        contact = data.get('contact')
        email = data.get('email')
        est_name = data.get('est_name')
        business_type = data.get('business_type')
        est_address = data.get('est_address')
        locality = data.get('locality')
        start_date = data.get('start_date')
        ownership_type = data.get('ownership_type')
        total_employees = data.get('total_employees')
        working_hours = data.get('working_hours')
        weekly_off = data.get('weekly_off')
        place = data.get('place')
        declaration_date = data.get('declaration_date')

        logger.debug(f"Received: {id_proof}, {full_name}, {father_or_husband}, {res_address}, {contact}, {email}, {est_name}, {business_type}, {est_address}, {locality}, {start_date}, {ownership_type}, {total_employees}, {working_hours}, {weekly_off}, {place}, {declaration_date}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO shop_establishment (id_proof, full_name, father_or_husband, res_address, contact, email, est_name, business_type, est_address, locality, start_date, ownership_type, total_employees, working_hours, weekly_off, place, declaration_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, full_name, father_or_husband, res_address, contact, email, est_name, business_type, est_address, locality, start_date, ownership_type, total_employees, working_hours, weekly_off, place, declaration_date))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Shop establishment submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /shop-establishment")
        return f"Internal Server Error: {e}", 500
    
@app.route('/fire-noc-form')
def fire_noc_form():
    return render_template('../html/fire.html')

@app.route('/fire-noc-form', methods=['POST'])
def submit_fire_noc_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        applicant_name = data.get('applicant_name')
        designation = data.get('designation')
        organization_name = data.get('organization_name')
        ownership_type = data.get('ownership_type')
        contact = data.get('contact')
        email = data.get('email')
        aadhaar_pan = data.get('aadhaar_pan')
        address = data.get('address')
        city = data.get('city')
        state = data.get('state')
        pincode = data.get('pincode')
        building_type = data.get('building_type')
        area = data.get('area')
        floors = data.get('floors')
        year_built = data.get('year_built')
        application_purpose = data.get('application_purpose')
        date = data.get('date')
        place = data.get('place')
        signature = data.get('signature')

        logger.debug(f"Received: {id_proof}, {applicant_name}, {designation}, {organization_name}, {ownership_type}, {contact}, {email}, {aadhaar_pan}, {address}, {city}, {state}, {pincode}, {building_type}, {area}, {floors}, {year_built}, {application_purpose}, {date}, {place}, {signature}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO fire_noc_applications (id_proof, applicant_name, designation, organization_name, ownership_type, contact, email, aadhaar_pan, address, city, state, pincode, building_type, area, floors, year_built, application_purpose, date, place, signature) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, applicant_name, designation, organization_name, ownership_type, contact, email, aadhaar_pan, address, city, state, pincode, building_type, area, floors, year_built, application_purpose, date, place, signature))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Fire NOC application submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /fire-noc-form")
        return f"Internal Server Error: {e}", 500

@app.route('/pollution-consent-form')
def pollution_form():
    return render_template('../html/pollution.html')

@app.route('/pollution-consent-form', methods=['POST'])
def submit_pollution_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        application_type = data.get('application_type')
        industry_name = data.get('industry_name')
        industry_type = data.get('industry_type')
        registered_address = data.get('registered_address')
        plant_address = data.get('plant_address')
        contact_number = data.get('contact_number')
        email = data.get('email')
        pan_gst = data.get('pan_gst')
        legal_status = data.get('legal_status')
        products = data.get('products')
        capacity = data.get('capacity')
        raw_materials = data.get('raw_materials')
        water_consumption = data.get('water_consumption')
        effluent_generated = data.get('effluent_generated')
        treatment_method = data.get('treatment_method')
        stack_emissions = data.get('stack_emissions')
        air_control_devices = data.get('air_control_devices')
        disposal_method = data.get('disposal_method')
        land_area = data.get('land_area')
        builtup_area = data.get('builtup_area')
        res_distance = data.get('res_distance')
        declarant_name = data.get('declarant_name')
        declarant_designation = data.get('declarant_designation')
        declaration_place = data.get('declaration_place')
        declaration_date = data.get('declaration_date')

        logger.debug(f"Received: {id_proof}, {application_type}, {industry_name}, {industry_type}, {registered_address}, {plant_address}, {contact_number}, {email}, {pan_gst}, {legal_status}, {products}, {capacity}, {raw_materials}, {water_consumption}, {effluent_generated}, {treatment_method}, {stack_emissions}, {air_control_devices}, {disposal_method}, {land_area}, {builtup_area}, {res_distance}, {declarant_name}, {declarant_designation}, {declaration_place}, {declaration_date}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO pollution_consent (id_proof, application_type, industry_name, industry_type, registered_address, plant_address, contact_number, email, pan_gst, legal_status, products, capacity, raw_materials, water_consumption, effluent_generated, treatment_method, stack_emissions, air_control_devices, disposal_method, land_area, builtup_area, res_distance, declarant_name, declarant_designation, declaration_place, declaration_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, application_type, industry_name, industry_type, registered_address, plant_address, contact_number, email, pan_gst, legal_status, products, capacity, raw_materials, water_consumption, effluent_generated, treatment_method, stack_emissions, air_control_devices, disposal_method, land_area, builtup_area, res_distance, declarant_name, declarant_designation, declaration_place, declaration_date))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Pollution consent submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /pollution-consent-form")
        return f"Internal Server Error: {e}", 500
@app.route('/iec-application')
def iec_form():
    return render_template('../html/import.html')
@app.route('/iec-application', methods=['POST'])
def submit_iec_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        applicant_name = data.get('applicant_name')
        applicant_type = data.get('applicant_type')
        pan = data.get('pan')
        gstin = data.get('gstin')
        entity_name = data.get('entity_name')
        nature_of_business = data.get('nature_of_business')
        establishment_date = data.get('establishment_date')
        address = data.get('address')
        state = data.get('state')
        pincode = data.get('pincode')
        email = data.get('email')
        mobile = data.get('mobile')
        bank_name = data.get('bank_name')
        branch_address = data.get('branch_address')
        account_number = data.get('account_number')
        ifsc = data.get('ifsc')

        logger.debug(f"Received: {id_proof}, {applicant_name}, {applicant_type}, {pan}, {gstin}, {entity_name}, {nature_of_business}, {establishment_date}, {address}, {state}, {pincode}, {email}, {mobile}, {bank_name}, {branch_address}, {account_number}, {ifsc}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO iec_applications (id_proof, applicant_name, applicant_type, pan, gstin, entity_name, nature_of_business, establishment_date, address, state, pincode, email, mobile, bank_name, branch_address, account_number, ifsc) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, applicant_name, applicant_type, pan, gstin, entity_name, nature_of_business, establishment_date, address, state, pincode, email, mobile, bank_name, branch_address, account_number, ifsc))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'IEC application submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /iec-application")
        return f"Internal Server Error: {e}", 500
    

@app.route('/enterprise-registration')
def enterprise_form():
    return render_template('../html/msme.html')

@app.route('/enterprise-registration', methods=['POST'])
def submit_enterprise_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        aadhaar_number = data.get('aadhaar_number')
        entrepreneur_name = data.get('entrepreneur_name')
        social_category = data.get('social_category')
        gender = data.get('gender')
        enterprise_name = data.get('enterprise_name')
        organization_type = data.get('organization_type')
        pan_number = data.get('pan_number')
        plant_address = data.get('plant_address')
        plant_district = data.get('plant_district')
        plant_state = data.get('plant_state')
        plant_pin = data.get('plant_pin')
        official_address = data.get('official_address')
        mobile = data.get('mobile')
        email = data.get('email')
        commencement_date = data.get('commencement_date')
        bank_name = data.get('bank_name')
        ifsc = data.get('ifsc')
        account_number = data.get('account_number')
        major_activity = data.get('major_activity')
        nic_primary = data.get('nic_primary')
        nic_additional = data.get('nic_additional')
        persons_employed = data.get('persons_employed')
        investment = data.get('investment')
        turnover = data.get('turnover')
        declaration = data.get('declaration')
        place = data.get('place')
        date = data.get('date')
        signature = data.get('signature')
        
        logger.debug(f"Received: {id_proof}, {aadhaar_number}, {entrepreneur_name}, {social_category}, {gender}, {enterprise_name}, {organization_type}, {pan_number}, {plant_address}, {plant_district}, {plant_state}, {plant_pin}, {official_address}, {mobile}, {email}, {commencement_date}, {bank_name}, {ifsc}, {account_number}, {major_activity}, {nic_primary}, {nic_additional}, {persons_employed}, {investment}, {turnover}, {declaration}, {place}, {date}, {signature}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO enterprise_registration (id_proof, aadhaar_number, entrepreneur_name, social_category, gender, enterprise_name, organization_type, pan_number, plant_address, plant_district, plant_state, plant_pin, official_address, mobile, email, commencement_date, bank_name, ifsc, account_number, major_activity, nic_primary, nic_additional, persons_employed, investment, turnover, declaration, place, date, signature) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, aadhaar_number, entrepreneur_name, social_category, gender, enterprise_name, organization_type, pan_number, plant_address, plant_district, plant_state, plant_pin, official_address, mobile, email, commencement_date, bank_name, ifsc, account_number, major_activity, nic_primary, nic_additional, persons_employed, investment, turnover, declaration, place, date, signature))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'Enterprise registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /enterprise-registration")
        return f"Internal Server Error: {e}", 500
    
@app.route('/gst-registration')
def gst_form():
    return render_template('../html/gst.html')

@app.route('/gst-registration', methods=['POST'])
def submit_gst_form():
    try:
        data = request.get_json()
        id_proof = data.get('id_proof')
        legal_name = data.get('legal_name')
        pan = data.get('pan')
        email = data.get('email')
        mobile = data.get('mobile')
        constitution = data.get('constitution')
        state = data.get('state')
        district = data.get('district')
        reason = data.get('reason')
        address1 = data.get('address1')
        address2 = data.get('address2')
        city = data.get('city')
        pincode = data.get('pincode')
        state2 = data.get('state2')
        bank_name = data.get('bank_name')
        account_no = data.get('account_no')
        ifsc = data.get('ifsc')
        goods = data.get('goods')
        services = data.get('services')
        auth_name = data.get('auth_name')
        auth_designation = data.get('auth_designation')
        auth_aadhaar = data.get('auth_aadhaar')
        auth_pan = data.get('auth_pan')
        auth_contact = data.get('auth_contact')

        logger.debug(f"Received: {id_proof}, {legal_name}, {pan}, {email}, {mobile}, {constitution}, {state}, {district}, {reason}, {address1}, {address2}, {city}, {pincode}, {state2}, {bank_name}, {account_no}, {ifsc}, {goods}, {services}, {auth_name}, {auth_designation}, {auth_aadhaar}, {auth_pan}, {auth_contact}")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO gst_registration (id_proof, legal_name, pan, email, mobile, constitution, state, district, reason, address1, address2, city, pincode, state2, bank_name, account_no, ifsc, goods, services, auth_name, auth_designation, auth_aadhaar, auth_pan, auth_contact) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                    (id_proof, legal_name, pan, email, mobile, constitution, state, district, reason, address1, address2, city, pincode, state2, bank_name, account_no, ifsc, goods, services, auth_name, auth_designation, auth_aadhaar, auth_pan, auth_contact))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'GST registration submitted successfully'}), 201
    except Exception as e:
        logger.exception("Error in /gst-registration")
        return f"Internal Server Error: {e}", 500
    
if __name__ == "__main__":
    app.run(debug=True)

    


