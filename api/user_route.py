from flask import Blueprint, request, jsonify
from models import User, CyberComplaint, PublicLimitedCompanyRegistration, CriminalComplaint, PropertyRegistration, LegalComplaint, MarriageComplaintForm, TrademarkComplaint, BarcodeRequest, ISOApplication, CopyrightRegistration, PatentApplication, StartupRegistration, LLCRegistration, CompanyRegistration, ChinaRegistration, WebServiceForm, ProprietorRegistration, PartnershipRegistration, OPCRegistration, PrivateCompanyRegistration, LLPRegistration, PublicLimitedCompanyRegistration, Sec8CompanyRegistration, NameRegistration, DirectorAppointment, CompanyWindingUp, CompanyStrikeoff, DinSurrender,TradeLicense, TradeLicenseRenewal, ShopEstablishment, FireNOCApplication, PollutionConsent, GSTRegistration, IECApplication, EnterpriseRegistration, GSTRegistration
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

@user_bp.route('/cyber-complaint', methods=['GET'])
def get_cyber_complaints():
    complaints = CyberComplaint.query.all()
    return jsonify([complaint.to_dict() for complaint in complaints])

@user_bp.route('/cyber-complaint', methods=['POST'])
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

@user_bp.route('/criminal-law-complaint', methods=['GET'])
def get_criminal_complaints():
    complaints = CriminalComplaint.query.all()
    return jsonify([complaint.to_dict() for complaint in complaints])

@user_bp.route('/criminal-law-complaint', methods=['POST'])
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
    try:
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
            documents=', '.join(data['documents']) if isinstance(data['documents'], list) else data['documents'],  # ✅ Convert list to string
            place=data['place'],
            date_filed=data['date_filed'],
            verified_by=data['verified_by'],
            verified_date=data['verified_date']
        )

        db.session.add(new_complaint)
        db.session.commit()

        return jsonify(new_complaint.to_dict()), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route('/submit-marriage-complaint', methods=['GET'])
def get_marriage_complaint():
    complaints = MarriageComplaintForm.query.all()
    return jsonify([complaint.to_dict() for complaint in complaints])

@user_bp.route('/submit-marriage-complaint', methods=['POST'])
def create_marriage_complaint():
    try:
        data = request.get_json()
        new_complaint = MarriageComplaintForm(
            id_proof=data['id_proof'],
            complainant_name=data['complainant_name'],
            comp_age=data['comp_age'],
            comp_gender=data['comp_gender'],
            comp_parent=data['comp_parent'],
            comp_address=data['comp_address'],
            comp_contact=data['comp_contact'],
            comp_email=data['comp_email'],
            spouse_name=data['spouse_name'],
            spouse_age=data['spouse_age'],
            spouse_gender=data['spouse_gender'],
            spouse_parent=data['spouse_parent'],
            spouse_address=data['spouse_address'],
            spouse_contact=data['spouse_contact'],
            spouse_email=data['spouse_email'],
            marriage_date=data['marriage_date'],
            marriage_place=data['marriage_place'],
            marriage_type=data['marriage_type'],
            marriage_cert_issued=data['marriage_cert_issued'],
            marriage_reg_applied=data['marriage_reg_applied'],
            reg_applied_date=data['reg_applied_date'],
            complaint_nature=data['complaint_nature']
        )
        db.session.add(new_complaint)
        db.session.commit()
        return jsonify(new_complaint.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500  

@user_bp.route('/trademark-complaint', methods=['GET'])
def get_trademark_complaint():
    complaints = TrademarkComplaint.query.all()
    return jsonify([complaint.to_dict() for complaint in complaints])

@user_bp.route('/trademark-complaint', methods=['POST'])
def create_trademark_complaint():
    try:
        data = request.get_json()
        new_complaint = TrademarkComplaint(
            id_proof=data['id_proof'],
            applicant_name=data['applicant_name'],
            applicant_type=data['applicant_type'],
            address=data['address'],
            state=data['state'],
            pin_code=data['pin_code'],
            email=data['email'],
            mobile=data['mobile'],
            nationality=data['nationality'],
            nature_of_business=data['nature_of_business'],
            trademark_name=data['trademark_name'],
            mark_type=data['mark_type'],
            logo=data['logo'],
            class_of_goods=data['class_of_goods'],
            description=data['description'],
            mark_used=data['mark_used'],
            first_use_date=data['first_use_date'],
            first_use_place=data['first_use_place'],
            priority_claim=data['priority_claim'],
            priority_country=data['priority_country'],
            priority_date=data['priority_date'],
            priority_app_no=data['priority_app_no'],
            agent_name=data['agent_name'],
            agent_reg_no=data['agent_reg_no'],
            power_of_attorney=data['power_of_attorney'],
            date=data['date'],
            place=data['place']
            )
        db.session.add(new_complaint)
        db.session.commit()
        return jsonify(new_complaint.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/barcode-request', methods=['GET'])
def get_barcode_request():
    requests = BarcodeRequest.query.all()
    return jsonify([request.to_dict() for request in requests])

@user_bp.route('/barcode-request', methods=['POST'])
def create_barcode_request():
    try:
        data = request.get_json()
        new_request = BarcodeRequest(
            id_proof=data['id_proof'],
            business_name=data['business_name'],
            contact_person=data['contact_person'],
            address=data['address'],
            phone=data['phone'],
            email=data['email'],
            gstin=data['gstin'],
            barcode_options=data['barcode_options'],
            barcode_format=data['barcode_format'],
            barcode_purpose=data['barcode_purpose'],
            declarant_name=data['declarant_name'],
            declaration_date=data['declaration_date'],
            submitted_at=data['submitted_at'],
            status=data['status'],
            remarks=data['remarks'],
            submitted_by=data['submitted_by']

        )
        db.session.add(new_request)
        db.session.commit()
        return jsonify(new_request.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/iso-application', methods=['GET'])
def get_iso_application():
    applications = ISOApplication.query.all()
    return jsonify([application.to_dict() for application in applications])

@user_bp.route('/iso-application', methods=['POST'])
def create_iso_application():
    try:
        data = request.get_json()
        new_application = ISOApplication(
            id_proof=data['id_proof'],
            org_name=data['org_name'],
            org_type=data['org_type'],
            address=data['address'],
            city=data['city'],
            state=data['state'],
            pin=data['pin'],
            country=data['country'],
            website=data['website'],
            establishment_year=data['establishment_year'],
            contact_name=data['contact_name'],
            designation=data['designation'],
            phone=data['phone'],
            mobile=data['mobile'],
            email=data['email'],
            cert_9001=data['cert_9001'],
            cert_14001=data['cert_14001'],
            cert_45001=data['cert_45001'],
            cert_22000=data['cert_22000'],
            cert_27001=data['cert_27001'],
            cert_other=data['cert_other'],
            scope=data['scope'],
            num_employees=data['num_employees'],
            num_sites=data['num_sites'],
            site_locations=data['site_locations'],
            cert_iso=data['cert_iso'],
            cert_msme=data['cert_msme'],
            cert_gst=data['cert_gst'],
            cert_other_name=data['cert_other_name'],
            lang_pref=data['lang_pref'],
            submit_date=data['submit_date'],
            submit_place=data['submit_place'],
            auth_name=data['auth_name'],
            auth_designation=data['auth_designation']
        )
        db.session.add(new_application)
        db.session.commit()
        return jsonify(new_application.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/copyright-registration', methods=['GET'])
def get_copyright_registration():
    registrations = CopyrightRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/copyright-registration', methods=['POST'])
def create_copyright_registration():
    try:
        data = request.get_json()
        new_registration = CopyrightRegistration(
            id_proof=data['id_proof'],
            type_of_work=data['type_of_work'],
            title=data['title'],
            language=data['language'],
            applicant_name=data['applicant_name'],
            applicant_address=data['applicant_address'],
            applicant_nationality=data['applicant_nationality'],
            applicant_contact=data['applicant_contact'],
            interest=data['interest'],
            published=data['published'],
            pub_date=data['pub_date'],
            pub_country=data['pub_country'],
            author_name=data['author_name'],
            author_address=data['author_address'],
            author_nationality=data['author_nationality'],
            author_deceased=data['author_deceased'],
            declaration_date=data['declaration_date'],
            declaration_place=data['declaration_place'],
            submit_date=data['submit_date']
            )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@user_bp.route('/submit-patent-application', methods=['GET'])
def get_patent_application():
    applications = PatentApplication.query.all()
    return jsonify([application.to_dict() for application in applications])

@user_bp.route('/submit-patent-application', methods=['POST'])
def create_patent_application():
    try:
        data = request.get_json()
        new_application = PatentApplication(
            id_proof=data['id_proof'],
            applicant_name=data['applicant_name'],
            applicant_nationality=data['applicant_nationality'],
            applicant_address=data['applicant_address'],
            applicant_contact=data['applicant_contact'],
            applicant_email=data['applicant_email'],
            category=data['category'],
            inventor1_name=data['inventor1_name'],
            inventor1_nationality=data['inventor1_nationality'],
            inventor1_address=data['inventor1_address'],
            inventor2_name=data['inventor2_name'],
            inventor2_nationality=data['inventor2_nationality'],
            inventor2_address=data['inventor2_address'],
            title=data['title'],
            application_type=data['application_type'],
            statement=data['statement'],
            inventor1_signature=data['inventor1_signature'],
            inventor2_signature=data['inventor2_signature'],
            attachments=data['attachments'],
            applicant_sign_name=data['applicant_sign_name'],
            place=data['place'],
            date=data['date'],
            signature=data['signature']
            )
        db.session.add(new_application)
        db.session.commit()
        return jsonify(new_application.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@user_bp.route('/startup-registration', methods=['GET'])
def get_startup_registration():
    registrations = StartupRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/startup-registration', methods=['POST'])
def create_startup_registration():
    try:
        data = request.get_json()
        new_registration = StartupRegistration(
            id_proof=data['id_proof'],
            entity_name=data['entity_name'],
            entity_type=data['entity_type'],
            reg_number=data['reg_number'],
            reg_date=data['reg_date'],
            cin=data['cin'],
            pan=data['pan'],
            website=data['website'],
            address=data['address'],
            city=data['city'],
            state=data['state'],
            pin=data['pin'],
            phone=data['phone'],
            email=data['email'],
            founder_name=data['founder_name'],
            founder_role=data['founder_role'],
            founder_mobile=data['founder_mobile'],
            founder_email=data['founder_email'],
            description=data['description'],
            innovation_type=data['innovation_type'],
            scalability=data['scalability'],
            funding_received=data['funding_received'],
            invester_name=data['invester_name'],
            funding_amount=data['funding_amount'],
            funding_date=data['funding_date'],
            submit_date=data['submit_date']
            )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict()), 201 
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/llc-registration', methods=['GET'])
def get_llc_registration():
    registrations = LLCRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/llc-registration', methods=['POST'])
def create_llc_registration():
    data = request.get_json()
    new_registration = LLCRegistration(
        id_proof=data['id_proof'],
        company_name=data['company_name'],
        buisness_address=data['buisness_address'],
        mailing_address=data['mailing_address'],
        agent_name=data['agent_name'],
        agent_address=data['agent_address'],
        buisness_phone=data['buisness_phone'],
        duration=data['duration'],
        submit_date=data['submit_date'],
        owner_name=data['owner_name'],
        owner_address=data['owner_address'],
        owner_email=data['owner_email'],
        owner_role=data['owner_role'],
        manager_name=data['manager_name'],
        manager_address=data['manager_address'],
        option=data['option'],
        organization_type=data['organization_type'],
        signature=data['signature'],
        submitted_date=data['submitted_date']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify(new_registration.to_dict()), 201

@user_bp.route('/company-registration', methods=['GET'])
def get_company_registration():
    registrations = CompanyRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/company-registration', methods=['POST'])
def create_company_registration():
    try:
        data = request.get_json()
        new_registration = CompanyRegistration(
            id_proof=data['id_proof'],
            proposed_name=data['proposed_name'],
            company_type=data['company_type'],
            registered_office_address=data['registered_office_address'],
            office_location=data['office_location'],
            director_name=data['director_name'],
            dob=data['dob'],
            nationality=data['nationality'],
            occupation=data['occupation'],
            service_address=data['service_address'],
            residential_address=data['residential_address'],
            secretary_name=data['secretary_name'],
            secretary_address=data['secretary_address'],
            total_shares=data['total_shares'],
            share_value=data['share_value'],
            currency=data['currency'],
            shareholder_1=data['shareholder_1'],
            shareholder_2=data['shareholder_2'],
            signature=data['signature'],
            submission_date=data['submission_date']
        )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict())  # ✅ No comma
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/china-registration', methods=['GET'])
def get_china_registration():
    registrations = ChinaRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/china-registration', methods=['POST'])
def create_china_registration():
    try:
        data = request.get_json()
        new_registration = ChinaRegistration(
            id_proof=data['id_proof'],
            company_name_chinese=data['company_name_chinese'],
            alternate_name=data['alternate_name'],
            company_type=data['company_type'],
            registered_address=data['registered_address'],
            business_scope=data['business_scope'],
            capital_rmb=data['capital_rmb'],
            operating_term=data['operating_term'],
            investor_name=data['investor_name'],
            investor_nationality=data['investor_nationality'],
            investor_id=data['investor_id'],
            investor_address=data['investor_address'],
            ownership_percent=data['ownership_percent'],
            legal_rep_name=data['legal_rep_name'],
            legal_rep_nationality=data['legal_rep_nationality'],
            legal_rep_id=data['legal_rep_id'],
            legal_rep_position=data['legal_rep_position'],
            supervisor_name=data['supervisor_name'],
            supervisor_contact=data['supervisor_contact'],
            executive_director=data['executive_director'],
            finance_manager=data['finance_manager'],
            contact_person_china=data['contact_person_china'],
            submitted_at=data['submitted_at']
            )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/web-service-form', methods=['GET'])
def get_web_service_form():
    forms = WebServiceForm.query.all()
    return jsonify([form.to_dict() for form in forms])

@user_bp.route('/web-service-form', methods=['POST'])
def create_web_service_form():
    try:
        data = request.get_json()
        new_registration = WebServiceForm(
            id_proof=data['id_proof'],
            full_name=data['full_name'],
            company_name=data['company_name'],
            email=data['email'],
            phone=data['phone'],
            address=data['address'],
            services=data['services'],
            project_description=data['project_description'],
            target_audience=data['target_audience'],
            existing_website=data['existing_website'],
            website_url=data['website_url'],
            preferred_technology=data['preferred_technology'],
            content_availability=data['content_availability'],
            example_websites=data['example_websites'],
            color_scheme=data['color_scheme'],
            start_date=data['start_date'],
            deadline=data['deadline'],
            budget_range=data['budget_range'],
            notes=data['notes'],
            signature=data['signature'],
            form_date=data['form_date']
            )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        

@user_bp.route('/proprietor-registration', methods=['GET'])
def get_proprietor_registration():
    registrations = ProprietorRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/proprietor-registration', methods=['POST'])
def create_proprietor_registration():
    try:
        data = request.get_json()
        new_registration = ProprietorRegistration(
            id_proof=data['id_proof'],
            full_name=data['full_name'],
            parent_name=data['parent_name'],
            dob=data['dob'],
            gender=data['gender'],
            aadhaar=data['aadhaar'],
            pan=data['pan'],
            mobile=data['mobile'],
            email=data['email'],
            res_address=data['res_address'],
            res_pin=data['res_pin'],
            firm_name=data['firm_name'],
            business_type=data['business_type'],
            nature=data['nature'],
            business_address=data['business_address'],
            business_city=data['business_city'],
            business_pin=data['business_pin'],
            commencement_date=data['commencement_date'],
            website=data['website'],
            bank_name=data['bank_name'],
            account_type=data['account_type'],
            ifsc=data['ifsc'],
            branch_address=data['branch_address'],
            registrations=data['registrations'],
            place=data['place'],
            declaration_date=data['declaration_date'],
            submitted_at=data['submitted_at']
            )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    

@user_bp.route('/partnership-form', methods=['GET'])
def get_partnership_form():
    registrations = PartnershipRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/partnership-form', methods=['POST'])
def create_partnership_form():
    try:
        data = request.get_json()
        new_registration = PartnershipRegistration(
            id_proof=data['id_proof'],
            firm_name=data['firm_name'],
            business_nature=data['business_nature'],
            address=data['address'],
            city=data['city'],
            state=data['state'],
            pincode=data['pincode'],
            phone=data['phone'],
            email=data['email'],
            commencement_date=data['commencement_date'],
            duration_type=data['duration_type'],
            duration_from=data['duration_from'],
            duration_to=data['duration_to'],
            partner_names=data['partner_names'],
            father_names=data['father_names'],
            partner_addresses=data['partner_addresses'],
            ages=data['ages'],
            pans=data['pans'],
            shares=data['shares'],
            capital_names=data['capital_names'],
            contributions=data['contributions'],
            bank_name=data['bank_name'],
            branch=data['branch'],
            account_number=data['account_number'],
            signature = data['signature'],
            submitted_date = data['submitted_at']
            )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
        

@user_bp.route('/opc-registration', methods=['GET'])
def get_opc_registration():
    registrations = OPCRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/opc-registration', methods=['POST'])
def create_opc_registration():
    try:
        data = request.get_json()
        new_registration = OPCRegistration(
            id_proof=data['id_proof'],
            company_name=data['company_name'],
            state=data['state'],
            auth_capital=data['auth_capital'],
            paid_capital=data['paid_capital'],
            main_activity=data['main_activity'],
            full_name=data['full_name'],
            father_name=data['father_name'],
            dob=data['dob'],
            nationality=data['nationality'],
            pan=data['pan'],
            aadhaar=data['aadhaar'],
            din=data['din'],
            mobile=data['mobile'],
            email=data['email'],
            res_address=data['res_address'],
            occupation=data['occupation'],
            nominee_name=data['nominee_name'],
            nominee_father=data['nominee_father'],
            nominee_dob=data['nominee_dob'],
            nominee_pan=data['nominee_pan'],
            nominee_aadhaar=data['nominee_aadhaar'],
            nominee_address=data['nominee_address'],
            nominee_relation=data['nominee_relation'],
            office_address=data['office_address'],
            office_city=data['office_city'],
            office_state=data['office_state'],
            office_pin=data['office_pin'],
            office_email=data['office_email'],
            office_phone=data['office_phone'],
            declarant_name=data['declarant_name'],
            declaration_date=data['declaration_date']
            )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict()), 201 
    except Exception as e:
        return jsonify({'error': str(e)}), 500 

@user_bp.route('/private-company-registration', methods=['GET'])
def get_private_company_registration():
    registrations = PrivateCompanyRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/private-company-registration', methods=['POST'])
def create_private_company_registration():
    try:
        data = request.get_json()
        new_registration = PrivateCompanyRegistration(
            id_proof=data['id_proof'],
            proposed_name=data['proposed_name'],
            business_activity=data['business_activity'],
            nic_code=data['nic_code'],
            objectives=data['objectives'],
            registered_office=data['registered_office'],
            email=data['email'],
            mobile=data['mobile'],
            authorized_capital=data['authorized_capital'],
            paidup_capital=data['paidup_capital'],
            director_name=data['director_name'],
            director_din=data['director_din'],
            director_address=data['director_address'],
            director_nationality=data['director_nationality'],
            director_role=data['director_role']
            )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict()), 201 
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/llp-registration', methods=['GET'])
def get_llp_registration():
    registrations = LLPRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/llp-registration', methods=['POST'])
def create_llp_registration():
    try:
        data = request.get_json()
        new_registration = LLPRegistration(
            id_proof=data['id_proof'],
            llp_name=data['llp_name'],
            nic_main=data['nic_main'],
            nic_desc=data['nic_desc'],
            address_line=data['address_line'],
            city=data['city'],
            state=data['state'],
            pincode=data['pincode'],
            email=data['email'],
            mobile=data['mobile'],
            partner1_name=data['partner1_name'],
            partner1_din=data['partner1_din'],
            partner1_pan=data['partner1_pan'],
            partner1_aadhaar=data['partner1_aadhaar'],
            partner1_address=data['partner1_address'],
            partner1_email=data['partner1_email'],
            partner1_mobile=data['partner1_mobile'],
            partner1_nationality=data['partner1_nationality'],
            partner1_occupation=data['partner1_occupation'],
            partner1_capital=data['partner1_capital'],
            partner2_name=data['partner2_name'],
            partner2_din=data['partner2_din'],
            partner2_pan=data['partner2_pan'],
            partner2_aadhaar=data['partner2_aadhaar'],
            partner2_address=data['partner2_address'],
            partner2_email=data['partner2_email'],
            partner2_mobile=data['partner2_mobile'],
            partner2_nationality=data['partner2_nationality'],
            partner2_occupation=data['partner2_occupation'],
            partner2_capital=data['partner2_capital'],
            total_capital=data['total_capital']
            )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/public-limited-registration', methods=['GET'])
def get_public_limited_registration():
    registrations = PublicLimitedCompanyRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/public-limited-registration', methods=['POST'])
def create_public_limited_registration():
    try:
        data = request.get_json()
        new_registration = PublicLimitedCompanyRegistration(
            id_proof=data['id_proof'],
            company_name_1=data['company_name_1'],
            company_name_2=data['company_name_2'],
            business_activity=data['business_activity'],
            authorized_capital=data['authorized_capital'],
            paidup_capital=data['paidup_capital'],
            address=data['address'],
            city=data['city'],
            state=data['state'],
            pin=data['pin'],
            email=data['email'],
            phone=data['phone'],
            main_object=data['main_object'],
            date=data['date'],
            place=data['place'],
            applicant_name=data['applicant_name'],
            signature=data['signature']
            )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/sec8-company-registration', methods=['GET'])
def get_sec8_company_registration():
    registrations = Sec8CompanyRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/sec8-company-registration', methods=['POST'])
def create_sec8_company_registration():
    try:
        data = request.get_json()
        new_registration = Sec8CompanyRegistration(
            id_proof=data['id_proof'],
            name_pref_1=data['name_pref_1'],
            name_pref_2=data['name_pref_2'],
            objectives=data['objectives'],
            nature_of_work=data['nature_of_work'],
            reg_address=data['reg_address'],
            reg_city=data['reg_city'],
            reg_state=data['reg_state'],
            reg_pincode=data['reg_pincode'],
            reg_email=data['reg_email'],
            reg_phone=data['reg_phone'],
            directors=data['directors'],
            authorized_capital=data['authorized_capital'],
            paid_up_capital=data['paid_up_capital']
            )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/name-registration', methods=['GET'])
def get_name_registration():
    registrations = NameRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/name-registration', methods=['POST'])
def create_name_registration():
    try:
        data = request.get_json()
        new_registration = NameRegistration(
            id_proof=data['id_proof'],
            current_name=data['current_name'],
            cin=data['cin'],
            company_type=data['company_type'],
            incorporation_date=data['incorporation_date'],
            registered_address=data['registered_address'],
            proposed_name=data['proposed_name'],
            name_srn=data['name_srn'],
            reason=data['reason'],
            board_meeting_date=data['board_meeting_date'],
            resolution_date=data['resolution_date'],
            director_name=data['director_name'],
            director_din=data['director_din'],
            submission_date=data['submission_date']
            )
        db.session.add(new_registration)
        db.session.commit()
        return jsonify(new_registration.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@user_bp.route('/director-appointment', methods=['GET'])
def get_director_appointment():
    registrations = DirectorAppointment.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/director-appointment', methods=['POST'])
def create_director_appointment():
    data = request.get_json()
    new_registration = DirectorAppointment(
        id_proof=data['id_proof'],
        company_name=data['company_name'],
        cin=data['cin'],
        reg_office=data['reg_office'],
        company_email=data['company_email'],
        full_name=data['full_name'],
        father_name=data['father_name'],
        din=data['din'],
        dob=data['dob'],
        nationality=data['nationality'],
        address=data['address'],
        email=data['email'],
        mobile=data['mobile'],
        occupation=data['occupation'],
        category=data['category'],
        appointment_date=data['appointment_date'],
        designation=data['designation'],
        consent_received=data['consent_received']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify(new_registration.to_dict()), 201

@user_bp.route('/address-change-form', methods=['GET'])
def get_address_change_form():
    registrations = AddressChangeForm.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/address-change-form', methods=['POST'])
def create_address_change_form():
    data = request.get_json()
    new_registration = AddressChangeForm(
        id_proof=data['id_proof'],
        full_name=data['full_name'],
        customer_id=data['customer_id'],
        phone=data['phone'],
        email=data['email'],
        old_address=data['old_address'],
        old_city=data['old_city'],
        old_state=data['old_state'],
        old_pincode=data['old_pincode'],
        new_address=data['new_address'],
        new_city=data['new_city'],
        new_state=data['new_state'],
        new_pincode=data['new_pincode'],
        effective_type=data['effective_type'],
        scheduled_date=data['scheduled_date'],
        signature=data['signature'],
        place=data['place'],
        form_date=data['form_date']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify(new_registration.to_dict()), 201

@user_bp.route('/company-winding-up', methods=['GET'])
def get_company_winding_up():
    registrations = CompanyWindingUp.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/company-winding-up', methods=['POST'])
def create_company_winding_up():
    data = request.get_json()
    new_registration = CompanyWindingUp(
        id_proof=data['id_proof'],
        company_name=data['company_name'],
        cin=data['cin'],
        registered_address=data['registered_address'],
        incorporation_date=data['incorporation_date'],
        authorized_capital=data['authorized_capital'],
        paid_up_capital=data['paid_up_capital'],
        mode=data['mode'],
        reason=data['reason'],
        board_resolution=data['board_resolution'],
        special_resolution=data['special_resolution'],
        declaration=data['declaration'],
        director1=data['director1'],
        director2=data['director2'],
        declaration_date=data['declaration_date']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify(new_registration.to_dict()), 201

@user_bp.route('/company-strikeoff', methods=['GET'])
def get_company_strikeoff():
    registrations = CompanyStrikeoff.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/company-strikeoff', methods=['POST'])
def create_company_strikeoff():
    data = request.get_json()
    new_registration = CompanyStrikeoff(
        id_proof=data['id_proof'],
        cin=data['cin'],
        company_name=data['company_name'],
        address=data['address'],
        email=data['email'],
        authorized_name=data['authorized_name'],
        designation=data['designation'],
        din=data['din'],
        contact=data['contact'],
        reason=data['reason'],
        other_reason=data['other_reason'],
        signature=data['signature'],
        declaration_date=data['declaration_date'],
        declaration_din=data['declaration_din']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify(new_registration.to_dict()), 201

@user_bp.route('/din-surrender', methods=['GET'])
def get_din_surrender():
    registrations = DinSurrender.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/din-surrender', methods=['POST'])
def create_din_surrender():
    data = request.get_json()
    new_registration = DinSurrender(
        id_proof=data['id_proof'],
        din=data['din'],
        reason=data['reason'],
        full_name=data['full_name'],
        father_name=data['father_name'],
        dob=data['dob'],
        gender=data['gender'],
        nationality=data['nationality'],
        pan=data['pan'],
        passport_no=data['passport_no'],
        address=data['address'],
        email=data['email'],
        mobile=data['mobile']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify(new_registration.to_dict()), 201 

@user_bp.route('/trade-license-registration', methods=['GET'])
def get_trade_license_registration():
    registrations = TradeLicense.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/trade-license-registration', methods=['POST'])
def create_trade_license_registration():
    data = request.get_json()
    new_registration = TradeLicense(
        id_proof=data['id_proof'],
        applicant_name=data['applicant_name'],
        father_or_spouse=data['father_or_spouse'],
        res_address=data['res_address'],
        mobile=data['mobile'],
        email=data['email'],
        business_type=data['business_type'],
        business_name=data['business_name'],
        business_address=data['business_address'],
        premises=data['premises'],
        ward=data['ward'],
        commencement_date=data['commencement_date'],
        employees=data['employees'],
        trade_classification=data['trade_classification'],
        place=data['place']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify(new_registration.to_dict()), 201
@user_bp.route('/trade-license-renewal', methods=['GET'])
def get_trade_license_renewal():
    registrations = TradeLicenseRenewal.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/trade-license-renewal', methods=['POST'])
def create_trade_license_renewal():
    data = request.get_json()
    new_registration = TradeLicenseRenewal(
        id_proof=data['id_proof'],
        applicant_name=data['applicant_name'],
        father_or_spouse=data['father_or_spouse'],
        res_address=data['res_address'],
        mobile=data['mobile'],
        email=data['email'],
        business_type=data['business_type'],
        business_name=data['business_name'],
        business_address=data['business_address'],
        premises=data['premises'],
        ward=data['ward'],
        commencement_date=data['commencement_date'],
        employees=data['employees'],
        trade_classification=data['trade_classification'],
        place=data['place']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify(new_registration.to_dict()), 201

@user_bp.route('/shop-establishment', methods=['GET'])
def get_shop_establishment():
    registrations = ShopEstablishment.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/shop-establishment', methods=['POST'])
def create_shop_establishment():
    data = request.get_json()
    new_registration = ShopEstablishment(
        id_proof=data['id_proof'],
        full_name=data['full_name'],
        father_or_husband=data['father_or_husband'],
        res_address=data['res_address'],
        contact=data['contact'],
        email=data['email'],
        est_name=data['est_name'],
        business_type=data['business_type'],
        est_address=data['est_address'],
        locality=data['locality'],
        start_date=data['start_date'],
        ownership_type=data['ownership_type'],
        total_employees=data['total_employees'],
        working_hours=data['working_hours'],
        weekly_off=data['weekly_off'],
        place=data['place'],
        declaration_date=data['declaration_date']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify(new_registration.to_dict()), 201

@user_bp.route('/fire-noc-form', methods=['GET'])
def get_fire_noc_form():
    registrations = FireNOCFormApplication.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/fire-noc-form', methods=['POST'])
def create_fire_noc_form():
    data = request.get_json()
    new_registration = FireNOCFormApplication(
        id_proof=data['id_proof'],
        applicant_name=data['applicant_name'],
        designation=data['designation'],
        organization_name=data['organization_name'],
        ownership_type=data['ownership_type'],
        contact=data['contact'],
        email=data['email'],
        aadhaar_pan=data['aadhaar_pan'],
        address=data['address'],
        city=data['city'],
        state=data['state'],
        pincode=data['pincode'],
        building_type=data['building_type'],
        area=data['area'],
        floors=data['floors'],
        year_built=data['year_built'],
        application_purpose=data['application_purpose'],
        date=data['date'],
        place=data['place'],
        signature=data['signature']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify(new_registration.to_dict()), 201

@user_bp.route('/pollution-consent', methods=['GET'])
def get_pollution_consent():
    registrations = PollutionConsent.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/pollution-consent', methods=['POST'])
def create_pollution_consent():
    data = request.get_json()
    new_registration = PollutionConsent(
        id_proof=data['id_proof'],
        application_type=data['application_type'],
        industry_name=data['industry_name'],
        industry_type=data['industry_type'],
        registered_address=data['registered_address'],
        plant_address=data['plant_address'],
        contact_number=data['contact_number'],
        email=data['email'],
        pan_gst=data['pan_gst'],
        legal_status=data['legal_status'],
        products=data['products'],
        capacity=data['capacity'],
        raw_materials=data['raw_materials'],
        water_consumption=data['water_consumption'],
        effluent_generated=data['effluent_generated'],
        treatment_method=data['treatment_method'],
        stack_emissions=data['stack_emissions'],
        air_control_devices=data['air_control_devices'],
        disposal_method=data['disposal_method'],
        land_area=data['land_area'],
        builtup_area=data['builtup_area'],
        res_distance=data['res_distance'],
        declarant_name=data['declarant_name'],
        declarant_designation=data['declarant_designation'],
        declaration_place=data['declaration_place'],
        declaration_date=data['declaration_date']
    )

@user_bp.route('/iec-application', methods=['GET'])
def get_iec_application():
    registrations = IECApplication.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/iec-application', methods=['POST'])
def create_iec_application():
    data = request.get_json()
    new_registration = IECApplication(
        id_proof=data['id_proof'],
        applicant_name=data['applicant_name'],
        applicant_type=data['applicant_type'],
        pan=data['pan'],
        gstin=data['gstin'],
        entity_name=data['entity_name'],
        nature_of_business=data['nature_of_business'],
        establishment_date=data['establishment_date'],
        address=data['address'],
        state=data['state'],
        pincode=data['pincode'],
        email=data['email'],
        mobile=data['mobile'],
        bank_name=data['bank_name'],
        branch_address=data['branch_address'],
        account_number=data['account_number'],
        ifsc=data['ifsc']
    )

@user_bp.route('/enterprise-registration', methods=['GET'])
def get_enterprise_registration():
    registrations = EnterpriseRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/enterprise-registration', methods=['POST'])
def create_enterprise_registration():
    data = request.get_json()
    new_registration = EnterpriseRegistration(
        id_proof=data['id_proof'],
        aadhaar_number=data['aadhaar_number'],
        entrepreneur_name=data['entrepreneur_name'],
        social_category=data['social_category'],
        gender=data['gender'],
        enterprise_name=data['enterprise_name'],
        organization_type=data['organization_type'],
        pan_number=data['pan_number'],
        plant_address=data['plant_address'],
        plant_district=data['plant_district'],
        plant_state=data['plant_state'],
        plant_pin=data['plant_pin'],
        official_address=data['official_address'],
        mobile=data['mobile'],
        email=data['email'],
        commencement_date=data['commencement_date'],
        bank_name=data['bank_name'],
        ifsc=data['ifsc'],
        account_number=data['account_number'],
        major_activity=data['major_activity'],
        nic_primary=data['nic_primary'],
        nic_additional=data['nic_additional'],
        persons_employed=data['persons_employed'],
        investment=data['investment'],
        turnover=data['turnover'],
        declaration=data['declaration'],
        place=data['place'],
        date=data['date'],
        signature=data['signature']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify(new_registration.to_dict()), 201

@user_bp.route('/gst-registration', methods=['GET'])
def get_gst_registration():
    registrations = GSTRegistration.query.all()
    return jsonify([registration.to_dict() for registration in registrations])

@user_bp.route('/gst-registration', methods=['POST'])
def create_gst_registration():
    data = request.get_json()
    new_registration = GSTRegistration(
        id_proof=data['id_proof'],
        legal_name=data['legal_name'],
        pan=data['pan'],
        email=data['email'],
        mobile=data['mobile'],
        constitution=data['constitution'],
        state=data['state'],
        district=data['district'],
        reason=data['reason'],
        address1=data['address1'],
        address2=data['address2'],
        city=data['city'],
        pincode=data['pincode'],
        state2=data['state2'],
        bank_name=data['bank_name'],
        account_no=data['account_no'],
        ifsc=data['ifsc'],
        goods=data['goods'],
        services=data['services'],
        auth_name=data['auth_name'],
        auth_designation=data['auth_designation'],
        auth_aadhaar=data['auth_aadhaar'],
        auth_pan=data['auth_pan'],
        auth_contact=data['auth_contact']
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify(new_registration.to_dict()), 201


