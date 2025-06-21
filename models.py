# models.py
from extensions import db
from datetime import datetime
import base64, json

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
    
class LegalComplaint(db.Model):
    __tablename__ = 'legal_complaints'
    
    id = db.Column(db.Integer, primary_key=True)
    case_no = db.Column(db.Text)
    complainant_name = db.Column(db.Text)
    complainant_address = db.Column(db.Text)
    complainant_contact = db.Column(db.Text)
    complainant_email = db.Column(db.Text)
    respondent_name = db.Column(db.Text)
    respondent_address = db.Column(db.Text)
    respondent_contact = db.Column(db.Text)
    respondent_email = db.Column(db.Text)
    relevant_act = db.Column(db.Text)
    complainant_full_name = db.Column(db.Text)
    complainant_full_address = db.Column(db.Text)
    complainant_contact_details = db.Column(db.Text)
    respondent_full_name = db.Column(db.Text)
    respondent_full_address = db.Column(db.Text)
    respondent_contact_details = db.Column(db.Text)
    facts = db.Column(db.Text)
    cause_of_action = db.Column(db.Text)
    relief_sought = db.Column(db.Text)

    # ✅ Changed from ARRAY to Text for compatibility
    documents = db.Column(db.Text)

    place = db.Column(db.Text)
    date_filed = db.Column(db.Date)
    verified_by = db.Column(db.Text)
    verified_date = db.Column(db.Date)

    def to_dict(self):
        return {
            "id": self.id,
            "case_no": self.case_no,
            "complainant_name": self.complainant_name,
            "complainant_address": self.complainant_address,
            "complainant_contact": self.complainant_contact,
            "complainant_email": self.complainant_email,
            "respondent_name": self.respondent_name,
            "respondent_address": self.respondent_address,
            "respondent_contact": self.respondent_contact,
            "respondent_email": self.respondent_email,
            "relevant_act": self.relevant_act,
            "complainant_full_name": self.complainant_full_name,
            "complainant_full_address": self.complainant_full_address,
            "complainant_contact_details": self.complainant_contact_details,
            "respondent_full_name": self.respondent_full_name,
            "respondent_full_address": self.respondent_full_address,
            "respondent_contact_details": self.respondent_contact_details,
            "facts": self.facts,
            "cause_of_action": self.cause_of_action,
            "relief_sought": self.relief_sought,

            # ✅ Convert back to list for API output
            "documents": self.documents.split(', ') if self.documents else [],

            "place": self.place,
            "date_filed": self.date_filed,
            "verified_by": self.verified_by,
            "verified_date": self.verified_date
        }

class MarriageComplaintForm(db.Model):
    __tablename__ = 'marriage_complaints'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    complainant_name = db.Column(db.Text)
    comp_age = db.Column(db.Text)
    comp_gender = db.Column(db.Text)
    comp_parent = db.Column(db.Text)
    comp_address = db.Column(db.Text)
    comp_contact = db.Column(db.Text)
    comp_email = db.Column(db.Text)
    spouse_name = db.Column(db.Text)
    spouse_age = db.Column(db.Text)
    spouse_gender = db.Column(db.Text)
    spouse_parent = db.Column(db.Text)
    spouse_address = db.Column(db.Text)
    spouse_contact = db.Column(db.Text)
    spouse_email = db.Column(db.Text)
    marriage_date = db.Column(db.Text)
    marriage_place = db.Column(db.Text)
    marriage_type = db.Column(db.Text)
    marriage_cert_issued = db.Column(db.Text)
    marriage_reg_applied = db.Column(db.Text)
    reg_applied_date = db.Column(db.Text)
    complaint_nature = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "complainant_name": self.complainant_name,
            "comp_age": self.comp_age,
            "comp_gender": self.comp_gender,
            "comp_parent": self.comp_parent,
            "comp_address": self.comp_address,
            "comp_contact": self.comp_contact,
            "comp_email": self.comp_email,
            "spouse_name": self.spouse_name,
            "spouse_age": self.spouse_age,
            "spouse_gender": self.spouse_gender,
            "spouse_parent": self.spouse_parent,
            "spouse_address": self.spouse_address,
            "spouse_contact": self.spouse_contact,
            "spouse_email": self.spouse_email,
            "marriage_date": self.marriage_date,
            "marriage_place": self.marriage_place,
            "marriage_type": self.marriage_type,
            "marriage_cert_issued": self.marriage_cert_issued,
            "marriage_reg_applied": self.marriage_reg_applied,
            "reg_applied_date": self.reg_applied_date,
            "complaint_nature": self.complaint_nature
        }

class TrademarkComplaint(db.Model):
    __tablename__ = 'trademark_applications'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    applicant_name = db.Column(db.Text)
    applicant_type = db.Column(db.Text)
    address = db.Column(db.Text)
    state = db.Column(db.Text)
    pin_code = db.Column(db.Text)
    email = db.Column(db.Text)
    mobile = db.Column(db.Text)
    nationality = db.Column(db.Text)
    nature_of_business = db.Column(db.Text)
    trademark_name = db.Column(db.Text)
    mark_type = db.Column(db.Text)
    logo = db.Column(db.Text)
    logo_filename = db.Column(db.Text)
    logo_mimetype = db.Column(db.Text)
    class_of_goods = db.Column(db.Text)
    description = db.Column(db.Text)
    mark_used = db.Column(db.Text)
    first_use_date = db.Column(db.Text)
    first_use_place = db.Column(db.Text)
    priority_claim = db.Column(db.Text)
    priority_country = db.Column(db.Text)
    priority_date = db.Column(db.Text)
    priority_app_no = db.Column(db.Text)
    agent_name = db.Column(db.Text)
    agent_reg_no = db.Column(db.Text)
    power_of_attorney = db.Column(db.Text)
    date = db.Column(db.Text)
    place = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "applicant_name": self.applicant_name,
            "applicant_type": self.applicant_type,
            "address": self.address,
            "state": self.state,
            "pin_code": self.pin_code,
            "email": self.email,
            "mobile": self.mobile,
            "nationality": self.nationality,
            "nature_of_business": self.nature_of_business,
            "trademark_name": self.trademark_name,
            "mark_type": self.mark_type,
            "logo": base64.b64encode(self.logo).decode('utf-8') if self.logo else None,
            "logo_filename": self.logo_filename,
            "logo_mimetype": self.logo_mimetype,
            "class_of_goods": self.class_of_goods,
            "description": self.description,
            "mark_used": self.mark_used,
            "first_use_date": self.first_use_date,
            "first_use_place": self.first_use_place,
            "priority_claim": self.priority_claim,
            "priority_country": self.priority_country,
            "priority_date": self.priority_date,
            "priority_app_no": self.priority_app_no,
            "agent_name": self.agent_name,
            "agent_reg_no": self.agent_reg_no,
            "power_of_attorney": self.power_of_attorney,
            "date": self.date,
            "place": self.place
        }

    def get_logo_base64(self):
        if self.logo:
            return base64.b64encode(self.logo.encode()).decode()
        return None
    
class BarcodeRequest(db.Model):
    __tablename__ = 'barcode_requests'
    business_name = db.Column(db.Text, primary_key=True)
    contact_person = db.Column(db.Text)
    address = db.Column(db.Text)
    phone = db.Column(db.Text)
    email = db.Column(db.Text)
    gstin = db.Column(db.Text)
    barcode_options = db.Column(db.Text)
    barcode_format = db.Column(db.Text)
    barcode_purpose = db.Column(db.Text)
    declarant_name = db.Column(db.Text)
    declaration_date = db.Column(db.Text)

    def to_dict(self):
        return {
            "business_name": self.business_name,
            "contact_person": self.contact_person,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "gstin": self.gstin,
            "barcode_options": self.barcode_options,
            "barcode_format": self.barcode_format,
            "barcode_purpose": self.barcode_purpose,
            "declarant_name": self.declarant_name,
            "declaration_date": self.declaration_date,
        }
class ISOApplication(db.Model):
    __tablename__ = 'iso_certifications'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    org_name = db.Column(db.Text)
    org_type = db.Column(db.Text)
    address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    pin = db.Column(db.Text)
    country = db.Column(db.Text)
    website = db.Column(db.Text)
    establishment_year = db.Column(db.Text)
    contact_name = db.Column(db.Text)
    designation = db.Column(db.Text)
    phone = db.Column(db.Text)
    mobile = db.Column(db.Text)
    email = db.Column(db.Text)
    cert_9001 = db.Column(db.Text)
    cert_14001 = db.Column(db.Text)
    cert_45001 = db.Column(db.Text)
    cert_22000 = db.Column(db.Text)
    cert_27001 = db.Column(db.Text)
    cert_other = db.Column(db.Text)
    scope = db.Column(db.Text)
    num_employees = db.Column(db.Text)
    num_sites = db.Column(db.Text)
    site_locations = db.Column(db.Text)
    cert_iso = db.Column(db.Text)
    cert_msme = db.Column(db.Text)
    cert_gst = db.Column(db.Text)
    cert_other_name = db.Column(db.Text)
    lang_pref = db.Column(db.Text)
    submit_date = db.Column(db.Text)
    submit_place = db.Column(db.Text)
    auth_name = db.Column(db.Text)
    auth_designation = db.Column(db.Text)
    def to_dict(self):
        return {
            "id": self.id,
            "org_name": self.org_name,
            "org_type": self.org_type,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "pin": self.pin,
            "country": self.country,
            "website": self.website,
            "establishment_year": self.establishment_year,
            "contact_name": self.contact_name,
            "designation": self.designation,
            "phone": self.phone,
            "mobile": self.mobile,
            "email": self.email,
            "cert_9001": self.cert_9001,
            "cert_14001": self.cert_14001,
            "cert_45001": self.cert_45001,
            "cert_22000": self.cert_22000,
            "cert_27001": self.cert_27001,
            "cert_other": self.cert_other,
            "scope": self.scope,
            "num_employees": self.num_employees,
            "num_sites": self.num_sites,
            "site_locations": self.site_locations,
            "cert_iso": self.cert_iso,
            "cert_msme": self.cert_msme,
            "cert_gst": self.cert_gst,
            "cert_other_name": self.cert_other_name,
            "lang_pref": self.lang_pref,
            "submit_date": self.submit_date,
            "submit_place": self.submit_place,
            "auth_name": self.auth_name,
            "auth_designation": self.auth_designation
        }
    
class CopyrightRegistration(db.Model):
    __tablename__ = 'copyright_registration'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    type_of_work = db.Column(db.Text)
    title = db.Column(db.Text)
    language = db.Column(db.Text)
    applicant_name = db.Column(db.Text)
    applicant_address = db.Column(db.Text)
    applicant_nationality = db.Column(db.Text)
    applicant_contact = db.Column(db.Text)
    interest = db.Column(db.Text)
    published = db.Column(db.Text)
    pub_date = db.Column(db.Text)
    pub_country = db.Column(db.Text)
    author_name = db.Column(db.Text)
    author_address = db.Column(db.Text)
    author_nationality = db.Column(db.Text)
    author_deceased = db.Column(db.Text)
    declaration_date = db.Column(db.Text)
    declaration_place = db.Column(db.Text)
    submit_date = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "type_of_work": self.type_of_work,
            "title": self.title,
            "language": self.language,
            "applicant_name": self.applicant_name,
            "applicant_address": self.applicant_address,
            "applicant_nationality": self.applicant_nationality,
            "applicant_contact": self.applicant_contact,
            "interest": self.interest,
            "published": self.published,
            "pub_date": self.pub_date,
            "pub_country": self.pub_country,
            "author_name": self.author_name,
            "author_address": self.author_address,
            "author_nationality": self.author_nationality,
            "author_deceased": self.author_deceased,
            "declaration_date": self.declaration_date,
            "declaration_place": self.declaration_place,
            "submit_date": self.submit_date
        }
class PatentApplication(db.Model):
    __tablename__ = 'patent_applications'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    applicant_name = db.Column(db.Text)
    applicant_nationality = db.Column(db.Text)
    applicant_address = db.Column(db.Text)
    applicant_contact = db.Column(db.Text)
    applicant_email = db.Column(db.Text)
    category = db.Column(db.Text)
    inventor1_name = db.Column(db.Text)
    inventor1_nationality = db.Column(db.Text)
    inventor1_address = db.Column(db.Text)
    inventor2_name = db.Column(db.Text)
    inventor2_nationality = db.Column(db.Text)
    inventor2_address = db.Column(db.Text)
    title = db.Column(db.Text)
    application_type = db.Column(db.Text)
    statement = db.Column(db.Text)
    inventor1_signature = db.Column(db.Text)
    inventor2_signature = db.Column(db.Text)
    attachments = db.Column(db.Text)
    applicant_sign_name = db.Column(db.Text)
    place = db.Column(db.Text)
    date = db.Column(db.Text)
    signature = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "applicant_name": self.applicant_name,
            "applicant_nationality": self.applicant_nationality,
            "applicant_address": self.applicant_address,
            "applicant_contact": self.applicant_contact,
            "applicant_email": self.applicant_email,
            "category": self.category,
            "inventor1_name": self.inventor1_name,
            "inventor1_nationality": self.inventor1_nationality,
            "inventor1_address": self.inventor1_address,
            "inventor2_name": self.inventor2_name,
            "inventor2_nationality": self.inventor2_nationality,
            "inventor2_address": self.inventor2_address,
            "title": self.title,
            "application_type": self.application_type,
            "statement": self.statement,
            "inventor1_signature": self.inventor1_signature,
            "inventor2_signature": self.inventor2_signature,
            "attachments": self.attachments,
            "applicant_sign_name": self.applicant_sign_name,
            "place": self.place,
            "date": self.date,
            "signature": self.signature
        }
    
class StartupRegistration(db.Model):
    __tablename__ = 'startup_registration'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    entity_name = db.Column(db.Text)
    entity_type = db.Column(db.Text)
    reg_number = db.Column(db.Text)
    reg_date = db.Column(db.Text)
    cin = db.Column(db.Text)
    pan = db.Column(db.Text)
    website = db.Column(db.Text)
    address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    pin = db.Column(db.Text)
    phone = db.Column(db.Text)
    email = db.Column(db.Text)
    founder_name = db.Column(db.Text)
    founder_role = db.Column(db.Text)
    founder_mobile = db.Column(db.Text)
    founder_email = db.Column(db.Text)
    description = db.Column(db.Text)
    innovation_type = db.Column(db.Text)
    scalability = db.Column(db.Text)
    funding_received = db.Column(db.Text)
    invester_name = db.Column(db.Text)
    funding_amount = db.Column(db.Text)
    funding_date = db.Column(db.Text)
    submit_date = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "entity_name": self.entity_name,
            "entity_type": self.entity_type,
            "reg_number": self.reg_number,
            "reg_date": self.reg_date,
            "cin": self.cin,
            "pan": self.pan,
            "website": self.website,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "pin": self.pin,
            "phone": self.phone,
            "email": self.email,
            "founder_name": self.founder_name,
            "founder_role": self.founder_role,
            "founder_mobile": self.founder_mobile,
            "founder_email": self.founder_email,
            "description": self.description,
            "innovation_type": self.innovation_type,
            "scalability": self.scalability,
            "funding_received": self.funding_received,
            "invester_name": self.invester_name,
            "funding_amount": self.funding_amount,
            "funding_date": self.funding_date,
            "submit_date": self.submit_date
        }
    
class LLCRegistration(db.Model):
    __tablename__ = 'llc_registrations'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    company_name = db.Column(db.Text)
    buisness_address = db.Column(db.Text)
    mailing_address = db.Column(db.Text)
    agent_name = db.Column(db.Text)
    agent_address = db.Column(db.Text)
    buisness_phone = db.Column(db.Text)
    duration = db.Column(db.Text)
    submit_date = db.Column(db.Text)
    owner_name = db.Column(db.Text)
    owner_address = db.Column(db.Text)
    owner_email = db.Column(db.Text)
    owner_role = db.Column(db.Text)
    manager_name = db.Column(db.Text)
    manager_address = db.Column(db.Text)
    option = db.Column(db.Text)
    organization_type = db.Column(db.Text)
    signature = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "company_name": self.company_name,
            "buisness_address": self.buisness_address,
            "mailing_address": self.mailing_address,
            "agent_name": self.agent_name,
            "agent_address": self.agent_address,
            "buisness_phone": self.buisness_phone,
            "duration": self.duration,
            "submit_date": self.submit_date,
            "owner_name": self.owner_name,
            "owner_address": self.owner_address,
            "owner_email": self.owner_email,
            "owner_role": self.owner_role,
            "manager_name": self.manager_name,
            "manager_address": self.manager_address,
            "option": self.option,
            "organization_type": self.organization_type,
            "signature": self.signature,
            "submit_date": self.submit_date
        }
    
class CompanyRegistration(db.Model):
    __tablename__ = 'uk_registration'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    proposed_name = db.Column(db.Text)
    company_type = db.Column(db.Text)
    registered_office_address = db.Column(db.Text)
    office_location = db.Column(db.Text)
    director_name = db.Column(db.Text)
    dob = db.Column(db.Text)
    nationality = db.Column(db.Text)
    occupation = db.Column(db.Text)
    service_address = db.Column(db.Text)
    residential_address = db.Column(db.Text)
    secretary_name = db.Column(db.Text)
    secretary_address = db.Column(db.Text)
    total_shares = db.Column(db.Text)
    share_value = db.Column(db.Text)
    currency = db.Column(db.Text)
    shareholder_1 = db.Column(db.Text)
    shareholder_2 = db.Column(db.Text)
    signature = db.Column(db.Text)
    submission_date = db.Column(db.Text)

    def to_dict(self):
        return {    
            "id": self.id,
            "id_proof": self.id_proof,
            "proposed_name": self.proposed_name,
            "company_type": self.company_type,
            "registered_office_address": self.registered_office_address,
            "office_location": self.office_location,
            "director_name": self.director_name,
            "dob": self.dob,    
            "nationality": self.nationality,
            "occupation": self.occupation,
            "service_address": self.service_address,
            "residential_address": self.residential_address,
            "secretary_name": self.secretary_name,
            "secretary_address": self.secretary_address,
            "total_shares": self.total_shares,
            "share_value": self.share_value,
            "currency": self.currency,
            "shareholder_1": self.shareholder_1,
            "shareholder_2": self.shareholder_2,
            "signature": self.signature,
            "submission_date": self.submission_date
        }

class ChinaRegistration(db.Model):
    __tablename__ = 'china_registration'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    company_name_chinese = db.Column(db.Text)
    alternate_name = db.Column(db.Text)
    company_type = db.Column(db.Text)
    registered_address = db.Column(db.Text)
    business_scope = db.Column(db.Text)
    capital_rmb = db.Column(db.Text)
    operating_term = db.Column(db.Text)
    investor_name = db.Column(db.Text)
    investor_nationality = db.Column(db.Text)
    investor_id = db.Column(db.Text)
    investor_address = db.Column(db.Text)
    ownership_percent = db.Column(db.Text)
    legal_rep_name = db.Column(db.Text)
    legal_rep_nationality = db.Column(db.Text)
    legal_rep_id = db.Column(db.Text)
    legal_rep_position = db.Column(db.Text)
    supervisor_name = db.Column(db.Text)
    supervisor_contact = db.Column(db.Text)
    executive_director = db.Column(db.Text)
    finance_manager = db.Column(db.Text)
    contact_person_china = db.Column(db.Text)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "company_name_chinese": self.company_name_chinese,
            "alternate_name": self.alternate_name,
            "company_type": self.company_type,
            "registered_address": self.registered_address,
            "business_scope": self.business_scope,
            "capital_rmb": self.capital_rmb,
            "operating_term": self.operating_term,
            "investor_name": self.investor_name,
            "investor_nationality": self.investor_nationality,
            "investor_id": self.investor_id,
            "investor_address": self.investor_address,
            "ownership_percent": self.ownership_percent,
            "legal_rep_name": self.legal_rep_name,
            "legal_rep_nationality": self.legal_rep_nationality,
            "legal_rep_id": self.legal_rep_id,
            "legal_rep_position": self.legal_rep_position,
            "supervisor_name": self.supervisor_name,
            "supervisor_contact": self.supervisor_contact,
            "executive_director": self.executive_director,
            "finance_manager": self.finance_manager,
            "contact_person_china": self.contact_person_china,
            "submitted_at": self.submitted_at
        }

class WebServiceForm(db.Model):
    __tablename__ = 'web_service_form'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    full_name = db.Column(db.Text)
    company_name = db.Column(db.Text)
    email = db.Column(db.Text)
    phone = db.Column(db.Text)
    address = db.Column(db.Text)
    services = db.Column(db.Text)
    project_description = db.Column(db.Text)
    target_audience = db.Column(db.Text)
    existing_website = db.Column(db.Text)
    website_url = db.Column(db.Text)
    preferred_technology = db.Column(db.Text)
    content_availability = db.Column(db.Text)
    example_websites = db.Column(db.Text)
    color_scheme = db.Column(db.Text)
    start_date = db.Column(db.Text)
    deadline = db.Column(db.Text)
    budget_range = db.Column(db.Text)
    notes = db.Column(db.Text)
    signature = db.Column(db.Text)
    form_date = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "full_name": self.full_name,
            "company_name": self.company_name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "services": self.services,
            "project_description": self.project_description,
            "target_audience": self.target_audience,
            "existing_website": self.existing_website,
            "website_url": self.website_url,
            "preferred_technology": self.preferred_technology,
            "content_availability": self.content_availability,
            "example_websites": self.example_websites,
            "color_scheme": self.color_scheme,
            "start_date": self.start_date,
            "deadline": self.deadline,
            "budget_range": self.budget_range,
            "notes": self.notes,
            "signature": self.signature,
            "form_date": self.form_date
        }

class ProprietorRegistration(db.Model):
    __tablename__ = 'proprietor_registration'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    full_name = db.Column(db.Text)
    parent_name = db.Column(db.Text)
    dob = db.Column(db.Text)
    gender = db.Column(db.Text)
    aadhaar = db.Column(db.Text)
    pan = db.Column(db.Text)
    mobile = db.Column(db.Text)
    email = db.Column(db.Text)
    res_address = db.Column(db.Text)
    res_pin = db.Column(db.Text)
    firm_name = db.Column(db.Text)
    business_type = db.Column(db.Text)
    nature = db.Column(db.Text)
    business_address = db.Column(db.Text)
    business_city = db.Column(db.Text)
    business_pin = db.Column(db.Text)
    commencement_date = db.Column(db.Text)
    website = db.Column(db.Text)
    bank_name = db.Column(db.Text)
    account_type = db.Column(db.Text)
    ifsc = db.Column(db.Text)
    branch_address = db.Column(db.Text)
    registrations = db.Column(db.Text)
    place = db.Column(db.Text)
    declaration_date = db.Column(db.Text)
    submitted_at = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "full_name": self.full_name,
            "parent_name": self.parent_name,
            "dob": self.dob,
            "gender": self.gender,
            "aadhaar": self.aadhaar,
            "pan": self.pan,
            "mobile": self.mobile,
            "email": self.email,
            "res_address": self.res_address,
            "res_pin": self.res_pin,
            "firm_name": self.firm_name,
            "business_type": self.business_type,
            "nature": self.nature,
            "business_address": self.business_address,
            "business_city": self.business_city,
            "business_pin": self.business_pin,
            "commencement_date": self.commencement_date,
            "website": self.website,
            "bank_name": self.bank_name,
            "account_type": self.account_type,
            "ifsc": self.ifsc,
            "branch_address": self.branch_address,
            "registrations": self.registrations,
            "place": self.place,
            "declaration_date": self.declaration_date,
            "submitted_at": self.submitted_at
        }
    
class PartnershipRegistration(db.Model):
    __tablename__ = 'partnership_registration'
    
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    firm_name = db.Column(db.Text)
    business_nature = db.Column(db.Text)
    address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    pincode = db.Column(db.Text)
    phone = db.Column(db.Text)
    email = db.Column(db.Text)
    commencement_date = db.Column(db.Text)
    duration_type = db.Column(db.Text)
    duration_from = db.Column(db.Text)
    duration_to = db.Column(db.Text)
    partner_names = db.Column(db.Text)
    father_names = db.Column(db.Text)
    partner_addresses = db.Column(db.Text)
    ages = db.Column(db.Text)
    pans = db.Column(db.Text)
    shares = db.Column(db.Text)
    capital_names = db.Column(db.Text)
    contributions = db.Column(db.Text)
    bank_name = db.Column(db.Text)
    branch = db.Column(db.Text)
    account_number = db.Column(db.Text)
    signature = db.Column(db.Text)          # ✅ Fixed
    submitted_at = db.Column(db.Text)       # ✅ Fixed

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "firm_name": self.firm_name,
            "business_nature": self.business_nature,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "pincode": self.pincode,
            "phone": self.phone,
            "email": self.email,
            "commencement_date": self.commencement_date,
            "duration_type": self.duration_type,
            "duration_from": self.duration_from,
            "duration_to": self.duration_to,
            "partner_names": self.partner_names,
            "father_names": self.father_names,
            "partner_addresses": self.partner_addresses,
            "ages": self.ages,
            "pans": self.pans,
            "shares": self.shares,
            "capital_names": self.capital_names,
            "contributions": self.contributions,
            "bank_name": self.bank_name,
            "branch": self.branch,
            "account_number": self.account_number,
            "signature": self.signature,
            "submitted_at": self.submitted_at
        }
class OPCRegistration(db.Model):
    __tablename__ = 'opc_registration'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    company_name = db.Column(db.Text)
    state = db.Column(db.Text)
    auth_capital = db.Column(db.Text)
    paid_capital = db.Column(db.Text)
    main_activity = db.Column(db.Text)
    full_name = db.Column(db.Text)
    father_name = db.Column(db.Text)
    dob = db.Column(db.Text)
    nationality = db.Column(db.Text)
    pan = db.Column(db.Text)
    aadhaar = db.Column(db.Text)
    din = db.Column(db.Text)
    mobile = db.Column(db.Text)
    email = db.Column(db.Text)
    res_address = db.Column(db.Text)
    occupation = db.Column(db.Text)
    nominee_name = db.Column(db.Text)
    nominee_father = db.Column(db.Text)
    nominee_dob = db.Column(db.Text)
    nominee_pan = db.Column(db.Text)
    nominee_aadhaar = db.Column(db.Text)
    nominee_address = db.Column(db.Text)
    nominee_relation = db.Column(db.Text)
    office_address = db.Column(db.Text)
    office_city = db.Column(db.Text)
    office_state = db.Column(db.Text)
    office_pin = db.Column(db.Text)
    office_email = db.Column(db.Text)
    office_phone = db.Column(db.Text)
    declarant_name = db.Column(db.Text)
    declaration_date = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "company_name": self.company_name,
            "state": self.state,
            "auth_capital": self.auth_capital,
            "paid_capital": self.paid_capital,
            "main_activity": self.main_activity,
            "full_name": self.full_name,
            "father_name": self.father_name,
            "dob": self.dob,
            "nationality": self.nationality,
            "pan": self.pan,
            "aadhaar": self.aadhaar,
            "din": self.din,
            "mobile": self.mobile,
            "email": self.email,
            "res_address": self.res_address,
            "occupation": self.occupation,
            "nominee_name": self.nominee_name,
            "nominee_father": self.nominee_father,
            "nominee_dob": self.nominee_dob,
            "nominee_pan": self.nominee_pan,
            "nominee_aadhaar": self.nominee_aadhaar,
            "nominee_address": self.nominee_address,
            "nominee_relation": self.nominee_relation,
            "office_address": self.office_address,
            "office_city": self.office_city,
            "office_state": self.office_state,
            "office_pin": self.office_pin,
            "office_email": self.office_email,
            "office_phone": self.office_phone,
            "declarant_name": self.declarant_name,
            "declaration_date": self.declaration_date
        }
    
class PrivateCompanyRegistration(db.Model):
    __tablename__ = 'private_company_registration'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    proposed_name = db.Column(db.Text)
    business_activity = db.Column(db.Text)
    nic_code = db.Column(db.Text)
    objectives = db.Column(db.Text)
    registered_office = db.Column(db.Text)
    email = db.Column(db.Text)
    mobile = db.Column(db.Text)
    authorized_capital = db.Column(db.Text)
    paidup_capital = db.Column(db.Text)
    director_name = db.Column(db.Text)
    director_din = db.Column(db.Text)
    director_address = db.Column(db.Text)
    director_nationality = db.Column(db.Text)
    director_role = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "proposed_name": self.proposed_name,
            "business_activity": self.business_activity,
            "nic_code": self.nic_code,
            "objectives": self.objectives,
            "registered_office": self.registered_office,
            "email": self.email,
            "mobile": self.mobile,
            "authorized_capital": self.authorized_capital,
            "paidup_capital": self.paidup_capital,
            "director_name": self.director_name,
            "director_din": self.director_din,
            "director_address": self.director_address,
            "director_nationality": self.director_nationality,
            "director_role": self.director_role
        }
    
class LLPRegistration(db.Model):
    __tablename__ = 'llp_registrations'
    id = db.Column(db.Integer, primary_key=True)
    llp_name = db.Column(db.Text)
    id_proof = db.Column(db.Text)
    name = db.Column(db.Text)
    nic_main = db.Column(db.Text)
    nic_desc = db.Column(db.Text)
    address_line = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    pincode = db.Column(db.Text)
    email = db.Column(db.Text)
    mobile = db.Column(db.Text)
    partner1_name = db.Column(db.Text)
    partner1_din = db.Column(db.Text)
    partner1_pan = db.Column(db.Text)
    partner1_aadhaar = db.Column(db.Text)
    partner1_address = db.Column(db.Text)
    partner1_email = db.Column(db.Text)
    partner1_mobile = db.Column(db.Text)
    partner1_nationality = db.Column(db.Text)
    partner1_occupation = db.Column(db.Text)
    partner1_capital = db.Column(db.Text)
    partner2_name = db.Column(db.Text)
    partner2_din = db.Column(db.Text)
    partner2_pan = db.Column(db.Text)
    partner2_aadhaar = db.Column(db.Text)
    partner2_address = db.Column(db.Text)
    partner2_email = db.Column(db.Text)
    partner2_mobile = db.Column(db.Text)
    partner2_nationality = db.Column(db.Text)
    partner2_occupation = db.Column(db.Text)
    partner2_capital = db.Column(db.Text)
    total_capital = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "name": self.name,
            "nic_main": self.nic_main,
            "nic_desc": self.nic_desc,
            "address_line": self.address_line,
            "city": self.city,
            "state": self.state,
            "pincode": self.pincode,
            "email": self.email,
            "mobile": self.mobile,
            "partner1_name": self.partner1_name,
            "partner1_din": self.partner1_din,
            "partner1_pan": self.partner1_pan,
            "partner1_aadhaar": self.partner1_aadhaar,
            "partner1_address": self.partner1_address,
            "partner1_email": self.partner1_email,
            "partner1_mobile": self.partner1_mobile,
            "partner1_nationality": self.partner1_nationality,
            "partner1_occupation": self.partner1_occupation,
            "partner1_capital": self.partner1_capital,
            "partner2_name": self.partner2_name,
            "partner2_din": self.partner2_din,
            "partner2_pan": self.partner2_pan,
            "partner2_aadhaar": self.partner2_aadhaar,
            "partner2_address": self.partner2_address,
            "partner2_email": self.partner2_email,
            "partner2_mobile": self.partner2_mobile,
            "partner2_nationality": self.partner2_nationality,
            "partner2_occupation": self.partner2_occupation,
            "partner2_capital": self.partner2_capital,
            "total_capital": self.total_capital
        }   

class PublicLimitedCompanyRegistration(db.Model):
    __tablename__ = 'public_limited_companies'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    company_name_1 = db.Column(db.Text)
    company_name_2 = db.Column(db.Text)
    business_activity = db.Column(db.Text)
    authorized_capital = db.Column(db.Text)
    paidup_capital = db.Column(db.Text)
    address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    pin = db.Column(db.Text)
    email = db.Column(db.Text)
    phone = db.Column(db.Text)
    main_object = db.Column(db.Text)
    date = db.Column(db.Text)
    place = db.Column(db.Text)
    applicant_name = db.Column(db.Text)
    signature = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "company_name_1": self.company_name_1,
            "company_name_2": self.company_name_2,
            "business_activity": self.business_activity,
            "authorized_capital": self.authorized_capital,
            "paidup_capital": self.paidup_capital,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "pin": self.pin,
            "email": self.email,
            "phone": self.phone,
            "main_object": self.main_object,
            "date": self.date,
            "place": self.place,
            "applicant_name": self.applicant_name,
            "signature": self.signature
        }
    
class Sec8CompanyRegistration(db.Model):
    __tablename__ = 'sec8_registration'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    name_pref_1 = db.Column(db.Text)
    name_pref_2 = db.Column(db.Text)
    objectives = db.Column(db.Text)
    nature_of_work = db.Column(db.Text)
    reg_address = db.Column(db.Text)
    reg_city = db.Column(db.Text)
    reg_state = db.Column(db.Text)
    reg_pincode = db.Column(db.Text)
    reg_email = db.Column(db.Text)
    reg_phone = db.Column(db.Text)
    directors = db.Column(db.Text)
    authorized_capital = db.Column(db.Text)
    paid_up_capital = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "name_pref_1": self.name_pref_1,
            "name_pref_2": self.name_pref_2,
            "objectives": self.objectives,
            "nature_of_work": self.nature_of_work,
            "reg_address": self.reg_address,
            "reg_city": self.reg_city,
            "reg_state": self.reg_state,
            "reg_pincode": self.reg_pincode,
            "reg_email": self.reg_email,
            "reg_phone": self.reg_phone,
            "directors": self.directors,
            "authorized_capital": self.authorized_capital,
            "paid_up_capital": self.paid_up_capital
        }
    
class NameRegistration(db.Model):
    __tablename__ = 'name_registration'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    current_name = db.Column(db.Text)
    cin = db.Column(db.Text)
    company_type = db.Column(db.Text)
    incorporation_date = db.Column(db.Text)
    registered_address = db.Column(db.Text)
    proposed_name = db.Column(db.Text)
    name_srn = db.Column(db.Text)
    reason = db.Column(db.Text)
    board_meeting_date = db.Column(db.Text)
    resolution_date = db.Column(db.Text)
    director_name = db.Column(db.Text)
    director_din = db.Column(db.Text)
    submission_date = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "current_name": self.current_name,
            "cin": self.cin,
            "company_type": self.company_type,
            "incorporation_date": self.incorporation_date,
            "registered_address": self.registered_address,
            "proposed_name": self.proposed_name,
            "name_srn": self.name_srn,
            "reason": self.reason,
            "board_meeting_date": self.board_meeting_date,
            "resolution_date": self.resolution_date,
            "director_name": self.director_name,
            "director_din": self.director_din,
            "submission_date": self.submission_date
        }
    
class DirectorAppointment(db.Model):
    __tablename__ = 'director_appointments'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    company_name = db.Column(db.Text)
    cin = db.Column(db.Text)
    reg_office = db.Column(db.Text)
    company_email = db.Column(db.Text)
    full_name = db.Column(db.Text)
    father_name = db.Column(db.Text)
    din = db.Column(db.Text)
    dob = db.Column(db.Text)
    nationality = db.Column(db.Text)
    address = db.Column(db.Text)
    email = db.Column(db.Text)
    mobile = db.Column(db.Text)
    occupation = db.Column(db.Text)
    category = db.Column(db.Text)
    appointment_date = db.Column(db.Text)
    designation = db.Column(db.Text)
    consent_received = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "company_name": self.company_name,
            "cin": self.cin,
            "reg_office": self.reg_office,
            "company_email": self.company_email,
            "full_name": self.full_name,
            "father_name": self.father_name,
            "din": self.din,
            "dob": self.dob,
            "nationality": self.nationality,
            "address": self.address,
            "email": self.email,
            "mobile": self.mobile,
            "occupation": self.occupation,
            "category": self.category,
            "appointment_date": self.appointment_date,
            "designation": self.designation,
            "consent_received": self.consent_received
        }

class AddressChangeRequest(db.Model):
    __tablename__ = 'address_change_requests'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    full_name = db.Column(db.Text)
    customer_id = db.Column(db.Text)
    phone = db.Column(db.Text)
    email = db.Column(db.Text)
    old_address = db.Column(db.Text)
    old_city = db.Column(db.Text)
    old_state = db.Column(db.Text)
    old_pincode = db.Column(db.Text)
    new_address = db.Column(db.Text)
    new_city = db.Column(db.Text)
    new_state = db.Column(db.Text)
    new_pincode = db.Column(db.Text)
    effective_type = db.Column(db.Text)
    scheduled_date = db.Column(db.Text)
    signature = db.Column(db.Text)
    place = db.Column(db.Text)
    form_date = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "full_name": self.full_name,
            "customer_id": self.customer_id,
            "phone": self.phone,
            "email": self.email,
            "old_address": self.old_address,
            "old_city": self.old_city,
            "old_state": self.old_state,
            "old_pincode": self.old_pincode,
            "new_address": self.new_address,
            "new_city": self.new_city,
            "new_state": self.new_state,
            "new_pincode": self.new_pincode,
            "effective_type": self.effective_type,
            "scheduled_date": self.scheduled_date,
            "signature": self.signature,
            "place": self.place,
            "form_date": self.form_date
        }
class CompanyWindingUp(db.Model):
    __tablename__ = 'company_winding_up'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    company_name = db.Column(db.Text)
    cin = db.Column(db.Text)
    registered_address = db.Column(db.Text)
    incorporation_date = db.Column(db.Text)
    authorized_capital = db.Column(db.Text)
    paid_up_capital = db.Column(db.Text)
    mode = db.Column(db.Text)
    reason = db.Column(db.Text)
    board_resolution = db.Column(db.Text)
    special_resolution = db.Column(db.Text)
    declaration = db.Column(db.Text)
    director1 = db.Column(db.Text)
    director2 = db.Column(db.Text)
    declaration_date = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "company_name": self.company_name,
            "cin": self.cin,
            "registered_address": self.registered_address,
            "incorporation_date": self.incorporation_date,
            "authorized_capital": self.authorized_capital,
            "paid_up_capital": self.paid_up_capital,
            "mode": self.mode,
            "reason": self.reason,
            "board_resolution": self.board_resolution,
            "special_resolution": self.special_resolution,
            "declaration": self.declaration,
            "director1": self.director1,
            "director2": self.director2,
            "declaration_date": self.declaration_date
        }
    
class CompanyStrikeoff(db.Model):
    __tablename__ = 'company_strikeoff'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    cin = db.Column(db.Text)
    company_name = db.Column(db.Text)
    address = db.Column(db.Text)
    email = db.Column(db.Text)
    authorized_name = db.Column(db.Text)
    designation = db.Column(db.Text)
    din = db.Column(db.Text)
    contact = db.Column(db.Text)
    reason = db.Column(db.Text)
    other_reason = db.Column(db.Text)
    signature = db.Column(db.Text)
    declaration_date = db.Column(db.Text)
    declaration_din = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "cin": self.cin,
            "company_name": self.company_name,
            "address": self.address,
            "email": self.email,
            "authorized_name": self.authorized_name,
            "designation": self.designation,
            "din": self.din,
            "contact": self.contact,
            "reason": self.reason,
            "other_reason": self.other_reason,
            "signature": self.signature,
            "declaration_date": self.declaration_date,
            "declaration_din": self.declaration_din
        }
class DinSurrender(db.Model):
    __tablename__ = 'din_surrender'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    din = db.Column(db.Text)
    reason = db.Column(db.Text)
    full_name = db.Column(db.Text)
    father_name = db.Column(db.Text)
    dob = db.Column(db.Text)
    gender = db.Column(db.Text)
    nationality = db.Column(db.Text)
    pan = db.Column(db.Text)
    passport_no = db.Column(db.Text)
    address = db.Column(db.Text)
    email = db.Column(db.Text)
    mobile = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "din": self.din,
            "reason": self.reason,
            "full_name": self.full_name,
            "father_name": self.father_name,
            "dob": self.dob,
            "gender": self.gender,
            "nationality": self.nationality,
            "pan": self.pan,
            "passport_no": self.passport_no,
            "address": self.address,
            "email": self.email,
            "mobile": self.mobile
        }
    
class TradeLicense(db.Model):
    __tablename__ = 'trade_license'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    applicant_name = db.Column(db.Text)
    father_or_spouse = db.Column(db.Text)
    res_address = db.Column(db.Text)
    mobile = db.Column(db.Text)
    email = db.Column(db.Text)
    business_type = db.Column(db.Text)
    business_name = db.Column(db.Text)
    business_address = db.Column(db.Text)
    premises = db.Column(db.Text)
    ward = db.Column(db.Text)
    commencement_date = db.Column(db.Text)
    employees = db.Column(db.Text)
    trade_classification = db.Column(db.Text)
    place = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "applicant_name": self.applicant_name,
            "father_or_spouse": self.father_or_spouse,
            "res_address": self.res_address,
            "mobile": self.mobile,
            "email": self.email,
            "business_type": self.business_type,
            "business_name": self.business_name,
            "business_address": self.business_address,
            "premises": self.premises,
            "ward": self.ward,
            "commencement_date": self.commencement_date,
            "employees": self.employees,
            "trade_classification": self.trade_classification,
            "place": self.place
        }
class TradeLicenseRenewal(db.Model):
    __tablename__ = 'trade_license_renewal'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    applicant_name = db.Column(db.Text)
    father_or_spouse = db.Column(db.Text)
    res_address = db.Column(db.Text)
    mobile = db.Column(db.Text)
    email = db.Column(db.Text)
    business_type = db.Column(db.Text)
    business_name = db.Column(db.Text)
    business_address = db.Column(db.Text)
    premises = db.Column(db.Text)
    ward = db.Column(db.Text)
    commencement_date = db.Column(db.Text)
    employees = db.Column(db.Text)
    trade_classification = db.Column(db.Text)
    place = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "applicant_name": self.applicant_name,
            "father_or_spouse": self.father_or_spouse,
            "res_address": self.res_address,
            "mobile": self.mobile,
            "email": self.email,
            "business_type": self.business_type,
            "business_name": self.business_name,
            "business_address": self.business_address,
            "premises": self.premises,
            "ward": self.ward,
            "commencement_date": self.commencement_date,
            "employees": self.employees,
            "trade_classification": self.trade_classification,
            "place": self.place
        }
class ShopEstablishment(db.Model):
    __tablename__ = 'shop_establishment'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    full_name = db.Column(db.Text)
    father_or_husband = db.Column(db.Text)
    res_address = db.Column(db.Text)
    contact = db.Column(db.Text)
    email = db.Column(db.Text)
    est_name = db.Column(db.Text)
    business_type = db.Column(db.Text)
    est_address = db.Column(db.Text)
    locality = db.Column(db.Text)
    start_date = db.Column(db.Text)
    ownership_type = db.Column(db.Text)
    total_employees = db.Column(db.Text)
    working_hours = db.Column(db.Text)
    weekly_off = db.Column(db.Text)
    place = db.Column(db.Text)
    declaration_date = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "full_name": self.full_name,
            "father_or_husband": self.father_or_husband,
            "res_address": self.res_address,
            "contact": self.contact,
            "email": self.email,
            "est_name": self.est_name,
            "business_type": self.business_type,
            "est_address": self.est_address,
            "locality": self.locality,
            "start_date": self.start_date,
            "ownership_type": self.ownership_type,
            "total_employees": self.total_employees,
            "working_hours": self.working_hours,
            "weekly_off": self.weekly_off,
            "place": self.place,
            "declaration_date": self.declaration_date
        }
class FireNOCApplication(db.Model):
    __tablename__ = 'fire_noc_applications'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    applicant_name = db.Column(db.Text)
    designation = db.Column(db.Text)
    organization_name = db.Column(db.Text)
    ownership_type = db.Column(db.Text)
    contact = db.Column(db.Text)
    email = db.Column(db.Text)
    aadhaar_pan = db.Column(db.Text)
    address = db.Column(db.Text)
    city = db.Column(db.Text)
    state = db.Column(db.Text)
    pincode = db.Column(db.Text)
    building_type = db.Column(db.Text)
    area = db.Column(db.Text)
    floors = db.Column(db.Text)
    year_built = db.Column(db.Text)
    application_purpose = db.Column(db.Text)
    date = db.Column(db.Text)
    place = db.Column(db.Text)
    signature = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "applicant_name": self.applicant_name,
            "designation": self.designation,
            "organization_name": self.organization_name,
            "ownership_type": self.ownership_type,
            "contact": self.contact,
            "email": self.email,
            "aadhaar_pan": self.aadhaar_pan,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "pincode": self.pincode,
            "building_type": self.building_type,
            "area": self.area,
            "floors": self.floors,
            "year_built": self.year_built,
            "application_purpose": self.application_purpose,
            "date": self.date,
            "place": self.place,
            "signature": self.signature
        }
class PollutionConsent(db.Model):
    __tablename__ = 'pollution_consent'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    application_type = db.Column(db.Text)
    industry_name = db.Column(db.Text)
    industry_type = db.Column(db.Text)
    registered_address = db.Column(db.Text)
    plant_address = db.Column(db.Text)
    contact_number = db.Column(db.Text)
    email = db.Column(db.Text)
    pan_gst = db.Column(db.Text)
    legal_status = db.Column(db.Text)
    products = db.Column(db.Text)
    capacity = db.Column(db.Text)
    raw_materials = db.Column(db.Text)
    water_consumption = db.Column(db.Text)
    effluent_generated = db.Column(db.Text)
    treatment_method = db.Column(db.Text)
    stack_emissions = db.Column(db.Text)
    air_control_devices = db.Column(db.Text)
    disposal_method = db.Column(db.Text)
    land_area = db.Column(db.Text)
    builtup_area = db.Column(db.Text)
    res_distance = db.Column(db.Text)
    declarant_name = db.Column(db.Text)
    declarant_designation = db.Column(db.Text)
    declaration_place = db.Column(db.Text)
    declaration_date = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "application_type": self.application_type,
            "industry_name": self.industry_name,
            "industry_type": self.industry_type,
            "registered_address": self.registered_address,
            "plant_address": self.plant_address,
            "contact_number": self.contact_number,
            "email": self.email,
            "pan_gst": self.pan_gst,
            "legal_status": self.legal_status,
            "products": self.products,
            "capacity": self.capacity,
            "raw_materials": self.raw_materials,
            "water_consumption": self.water_consumption,
            "effluent_generated": self.effluent_generated,
            "treatment_method": self.treatment_method,
            "stack_emissions": self.stack_emissions,
            "air_control_devices": self.air_control_devices,
            "disposal_method": self.disposal_method,
            "land_area": self.land_area,
            "builtup_area": self.builtup_area,
            "res_distance": self.res_distance,
            "declarant_name": self.declarant_name,
            "declarant_designation": self.declarant_designation,
            "declaration_place": self.declaration_place,
            "declaration_date": self.declaration_date
        }
class IECApplication(db.Model):
    __tablename__ = 'iec_applications'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    applicant_name = db.Column(db.Text)
    applicant_type = db.Column(db.Text)
    pan = db.Column(db.Text)
    gstin = db.Column(db.Text)
    entity_name = db.Column(db.Text)
    nature_of_business = db.Column(db.Text)
    establishment_date = db.Column(db.Text)
    address = db.Column(db.Text)
    state = db.Column(db.Text)
    pincode = db.Column(db.Text)
    email = db.Column(db.Text)
    mobile = db.Column(db.Text)
    bank_name = db.Column(db.Text)
    branch_address = db.Column(db.Text)
    account_number = db.Column(db.Text)
    ifsc = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "applicant_name": self.applicant_name,
            "applicant_type": self.applicant_type,
            "pan": self.pan,
            "gstin": self.gstin,
            "entity_name": self.entity_name,
            "nature_of_business": self.nature_of_business,
            "establishment_date": self.establishment_date,
            "address": self.address,
            "state": self.state,
            "pincode": self.pincode,
            "email": self.email,
            "mobile": self.mobile,
            "bank_name": self.bank_name,
            "branch_address": self.branch_address,
            "account_number": self.account_number,
            "ifsc": self.ifsc
        }
    
class EnterpriseRegistration(db.Model):
    __tablename__ = 'enterprise_registration'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    aadhaar_number = db.Column(db.Text)
    entrepreneur_name = db.Column(db.Text)
    social_category = db.Column(db.Text)
    gender = db.Column(db.Text)
    enterprise_name = db.Column(db.Text)
    organization_type = db.Column(db.Text)
    pan_number = db.Column(db.Text)
    plant_address = db.Column(db.Text)
    plant_district = db.Column(db.Text)
    plant_state = db.Column(db.Text)
    plant_pin = db.Column(db.Text)
    official_address = db.Column(db.Text)
    mobile = db.Column(db.Text)
    email = db.Column(db.Text)
    commencement_date = db.Column(db.Text)
    bank_name = db.Column(db.Text)
    ifsc = db.Column(db.Text)
    account_number = db.Column(db.Text)
    major_activity = db.Column(db.Text)
    nic_primary = db.Column(db.Text)
    nic_additional = db.Column(db.Text)
    persons_employed = db.Column(db.Text)
    investment = db.Column(db.Text)
    turnover = db.Column(db.Text)
    declaration = db.Column(db.Text)
    place = db.Column(db.Text)
    date = db.Column(db.Text)
    signature = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "aadhaar_number": self.aadhaar_number,
            "entrepreneur_name": self.entrepreneur_name,
            "social_category": self.social_category,
            "gender": self.gender,
            "enterprise_name": self.enterprise_name,
            "organization_type": self.organization_type,
            "pan_number": self.pan_number,
            "plant_address": self.plant_address,
            "plant_district": self.plant_district,
            "plant_state": self.plant_state,
            "plant_pin": self.plant_pin,
            "official_address": self.official_address,
            "mobile": self.mobile,
            "email": self.email,
            "commencement_date": self.commencement_date,
            "bank_name": self.bank_name,
            "ifsc": self.ifsc,
            "account_number": self.account_number,
            "major_activity": self.major_activity,
            "nic_primary": self.nic_primary,
            "nic_additional": self.nic_additional,
            "persons_employed": self.persons_employed,
            "investment": self.investment,
            "turnover": self.turnover,
            "declaration": self.declaration,
            "place": self.place,
            "date": self.date,
            "signature": self.signature
        }
    
class GSTRegistration(db.Model):
    __tablename__ = 'gst_registration'
    id = db.Column(db.Integer, primary_key=True)
    id_proof = db.Column(db.Text)
    legal_name = db.Column(db.Text)
    pan = db.Column(db.Text)
    email = db.Column(db.Text)
    mobile = db.Column(db.Text)
    constitution = db.Column(db.Text)
    state = db.Column(db.Text)
    district = db.Column(db.Text)
    reason = db.Column(db.Text)
    address1 = db.Column(db.Text)
    address2 = db.Column(db.Text)
    city = db.Column(db.Text)
    pincode = db.Column(db.Text)
    state2 = db.Column(db.Text)
    bank_name = db.Column(db.Text)
    account_no = db.Column(db.Text)
    ifsc = db.Column(db.Text)
    goods = db.Column(db.Text)
    services = db.Column(db.Text)
    auth_name = db.Column(db.Text)
    auth_designation = db.Column(db.Text)
    auth_aadhaar = db.Column(db.Text)
    auth_pan = db.Column(db.Text)
    auth_contact = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "id_proof": self.id_proof,
            "legal_name": self.legal_name,
            "pan": self.pan,
            "email": self.email,
            "mobile": self.mobile,
            "constitution": self.constitution,
            "state": self.state,
            "district": self.district,
            "reason": self.reason,
            "address1": self.address1,
            "address2": self.address2,
            "city": self.city,
            "pincode": self.pincode,
            "state2": self.state2,
            "bank_name": self.bank_name,
            "account_no": self.account_no,
            "ifsc": self.ifsc,
            "goods": self.goods,
            "services": self.services,
            "auth_name": self.auth_name,
            "auth_designation": self.auth_designation,
            "auth_aadhaar": self.auth_aadhaar,
            "auth_pan": self.auth_pan,
            "auth_contact": self.auth_contact
        }