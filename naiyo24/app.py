from flask import Flask, render_template, request, redirect, jsonify
from extensions import db
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

