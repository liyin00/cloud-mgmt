# Might change this to using os.environ.get() instead in future sprints
from unicodedata import name
from decouple import config
from flask import Flask, json, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
import hashlib

# from classes import *

# Database connection

# EC2 DB port is 3306 instead, change accordingly.
app = Flask(__name__)
# EC2 DB port is 3306 instead, change accordingly.
#
# app.config['SQLALCHEMY_DATABASE_URI'] = config('dbURL') or  environ.get("dbURL")
# # app.config['SQLALCHEMY_DATABASE_URI'] = config('localURL') or environ.get('localURL')

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
#                                            'pool_recycle': 280}

PASSWORD =os.getenv('PASSWORD') or  environ.get("PASSWORD")
PUBLIC_IP_ADDRESS =os.getenv('PUBLIC_IP_ADDRESS') or  environ.get("PUBLIC_IP_ADDRESS")
DBNAME =os.getenv('DBNAME') or  environ.get("DBNAME")
PROJECT_ID =os.getenv('PROJECT_ID') or  environ.get("PROJECT_ID")
INSTANCE_NAME =os.getenv('INSTANCE_NAME') or  environ.get("INSTANCE_NAME")
 
# configuration
# app.config["SECRET_KEY"] = "yoursecretkey"
# app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+pymysql://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}:3306/{DBNAME}"
# app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True

db = SQLAlchemy(app)

CORS(app)

class User(db.Model):
    __tablename__ = "User"
    user_id = db.Column(db.String(500),primary_key=True, nullable=False)
    email = db.Column(db.String(500), nullable=False)
    name = db.Column(db.String(500), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    creation_date = db.Column(db.String(500), nullable=False)


    def json(self):
        user_detail = {
            'user_id': self.user_id,
            'email': self.email,
            'name': self.name,
            'creation_date': self.creation_date
        }
        return user_detail

@app.route("/myenv", methods=['GET'])
def myenv():
    creds = "Password is" + str(PASSWORD) + " IP is " + str(PUBLIC_IP_ADDRESS) + " Database Name is " + str(DBNAME) + " Project ID is " + str(PROJECT_ID) + " Instance Name is " + str(INSTANCE_NAME)
    return creds

@app.route("/get_user_info/<string:email>", methods=['GET'])
def get_user_info(email):
    try:
        # data = request.get_json()
        # user_id = data['user_id']

        user_detail = User.query.filter_by(email=email).first()
        if not user_detail:
            return jsonify(
                {
                    "code": 404,
                    "message": "email not found."
                }
            ), 404
        
        return jsonify(
            {
                "code": 200,
                "data": user_detail.json(),
                "message": "successfully retrieved"
            }
        ), 200
        
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while getting the order. " + str(e)
            }
        ), 500

@app.route("/login", methods=['POST'])
def login():
    #insert into class record, update slot available, delete from registration
    try:

        data = request.get_json()

        db_password = data['password']
        h = hashlib.md5(db_password.encode())
        password = h.hexdigest()

        user_detail = User.query.filter_by(email=data['email']).first()

        if(user_detail.password == password):
            return jsonify(
            {
                "code": 200,
                "message": "Successfully login"

            }
            )
        return jsonify(
            {
                "code": 404,
                 "message": "password is incorrect"
            }
            )


    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occur when log in" + str(e)
            }
        ), 500

if __name__ == '__main__':
    print("users ")
    app.run(host='0.0.0.0', port=5003, debug=True)