from flask import Flask, render_template, request, redirect, jsonify
from extensions import db
import psycopg2
import logging
from flask_cors import CORS
from api.user_route import user_bp, contact_bp 

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Kanna_0744@localhost/naiyo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True

db.init_app(app)
app.register_blueprint(user_bp)
app.register_blueprint(contact_bp)

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

        logger.debug(f"Received: {name}, {email}, {phone}, {message}")

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (name, email, phone, message) VALUES (%s, %s, %s, %s)',
                    (name, email, phone, message))
        conn.commit()
        cur.close()
        conn.close()

        return redirect('/')
    
    except Exception as e:
        logger.exception("Error in /submit")
        return f"Internal Server Error: {e}", 500


def get_db_connection():
    return psycopg2.connect(
        host='localhost',
        database='naiyo',
        user='postgres',
        password='Kanna_0744'
    )

@app.route('/contacts', methods=['POST'])
def regist():
    try:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        aadhar = request.form['aadhar']
        how = request.form['how']

        logger.debug(f"Received: {name}, {email}, {phone}, {aadhar}, {how}")

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO list (name, email, phone, aadhar, how) VALUES (%s, %s, %s, %s, %s)',
                    (name, email, phone, aadhar, how))
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'status': 'success', 'message': 'Contact submitted successfully'}), 200

    
    except Exception as e:
        logger.exception("Error in /contacts")
        return f"Internal Server Error: {e}", 500

@app.route('/late')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM list')
    contacts = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('late.html', contact=contacts)
