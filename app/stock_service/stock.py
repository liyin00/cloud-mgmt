# Might change this to using os.environ.get() instead in future sprints
from decouple import config
from flask import Flask, json, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
from datetime import datetime
## new
import os
from dotenv import load_dotenv
load_dotenv()
# from classes import *

# Database connection

# EC2 DB port is 3306 instead, change accordingly.
app = Flask(__name__)

PASSWORD =os.getenv('PASSWORD') or  environ.get("PASSWORD")
PUBLIC_IP_ADDRESS =os.getenv('PUBLIC_IP_ADDRESS') or  environ.get("PUBLIC_IP_ADDRESS")
DBNAME =os.getenv('DBNAME') or  environ.get("DBNAME")
PROJECT_ID =os.getenv('PROJECT_ID') or  environ.get("PROJECT_ID")
# INSTANCE_NAME =os.getenv('INSTANCE_NAME') or  environ.get("INSTANCE_NAME")
 
# configuration
# app.config["SECRET_KEY"] = "yoursecretkey"
# app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket=/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+pymysql://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}:3306/{DBNAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
db = SQLAlchemy(app)

CORS(app)

class Stock(db.Model):
    __tablename__ = "Stock"
    product_id = db.Column(db.String(500),primary_key=True, nullable=False)
    quantity = db.Column(db.String(500), nullable=False)

    def create_stock(self):
        try:
            print("test")
            db.session.add(self)
            db.session.commit()
            return 200
        except Exception as e:
            print("testy")
            return 502

    def json(self):
        product_detail = {
            'product_id': self.product_id,
            'quantity': self.quantity
        }
        return product_detail


@app.route("/update_deduct_stock_by_product_id", methods=['PUT'])
def update_deduct_stock_by_product_id():
    try:
        data = request.get_json()
        product_id = data['product_id']
        quantity = data['quantity']

        stock = Stock.query.filter_by(product_id=product_id).first()
        if not stock:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "product_id": product_id
                    },
                    "message": "product_id not found."
                }
            ), 404
        
        quantity = int(stock.quantity) - int(quantity)
        if(quantity >= 0):
            stock.quantity = str(quantity)
        #reduce by 1
            db.session.commit()
            
            return jsonify(
                {
                    "code": 200,
                    "data": stock.json(),
                    "message": "successfully updated stock"
                }
            ), 200
        else:
            return jsonify(
                {
                    "code": 400,
                    "data": stock.json(),
                    "message" :"please check on quantity before ordering"

                    
                }
            ), 200


    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "product_id": product_id
                },
                "message": "An error occurred while updating the stock. " + str(e)
            }
        ), 500

#class id is ME111_C1
@app.route("/get_stock_by_product_id/<string:product_id>")
def get_stock_by_product_id(product_id):
    #registration, course, class table # course_id etc
    print("test")
    try:
        stock_detail = Stock.query.filter_by(product_id = product_id).first()
        if stock_detail:
            return jsonify(
                {
                    'code': 200,
                        'data': stock_detail.json()

                }
            )
        return jsonify(
            {
                'code': 400,
                    'data': {
                    "product_id": product_id
                    },
                "message": "An error occurred while retrieve the stock for product" + str(product_id) + " error:" + str(e)

            }
        )       
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "product_id": product_id
                },
                "message": "An error occurred while retrieve the stock for product" + str(product_id) + " error:" + str(e)
            }
        ), 500



#perform by admin
@app.route("/update_stock_by_product_id", methods=['PUT'])
def update_stock_by_product_id():
    try:
        data = request.get_json()
        product_id = data['product_id']
        quantity = data['quantity']

        stock = Stock.query.filter_by(product_id=product_id).first()
        if not stock:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "product_id": product_id
                    },
                    "message": "product_id" + str(product_id) +  "not found."
                }
            ), 404
        if(int(quantity) < 0 ):
            return jsonify(
            {
                "code": 400,
                "data": stock.json(),
                "message": "Please enter a positive stock number"
            }
        ), 200
        stock.quantity = quantity

        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": stock.json(),
                "message": "successfully updated stock"
            }
        ), 200



    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "product_id": product_id
                },
                "message": "An error occurred while updating the stock for product" + str(product_id) + " error:" + str(e)
            }
        ), 500


#sequential , after admin create product, should create stock
@app.route("/create_stock", methods=['POST'])
def create_stock():
    #insert into class record, update slot available, delete from registration
    try:
        #retrieve id 
        data = request.get_json()

        # Should immediately exit upon failing this line.....
        
        stock_record = Stock(
            product_id=data['product_id'],
            quantity = data['quantity']
            
        )
        print("come here")
        insert_code = stock_record.create_stock()

        return jsonify(
            {
                "code": insert_code
            }
        )

    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occur when update the slot " + str(e)
            }
        ), 500

if __name__ == '__main__':
    print("stock")
    app.run(host='0.0.0.0', port=5001, debug=True)