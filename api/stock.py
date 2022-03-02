# Might change this to using os.environ.get() instead in future sprints
from decouple import config
from flask import Flask, json, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
from datetime import datetime
# from classes import *

# Database connection

# EC2 DB port is 3306 instead, change accordingly.
app = Flask(__name__)
# EC2 DB port is 3306 instead, change accordingly.
#config('dbURL') or 
app.config['SQLALCHEMY_DATABASE_URI'] =  config('dbURL') or  environ.get("dbURL")
# app.config['SQLALCHEMY_DATABASE_URI'] = config('localURL') or environ.get('localURL')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class Stock(db.Model):
    __tablename__ = "Stock"
    product_id = db.Column(db.String(500),primary_key=True, nullable=False)
    stock_count = db.Column(db.String(500), nullable=False)


    def json(self):
        product_detail = {
            'product_id': self.product_id,
            'stock_count': self.stock_count
        }
        return product_detail


@app.route("/update_stock_by_pid", methods=['PUT'])
def update_stock():
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
        
        quantity = int(stock.stock_count) - int(quantity)
        stock.stock_count = str(quantity)
        #reduce by 1
        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": stock.json()
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
    stock_detail = Stock.query.filter_by(product_id = product_id).first()
    return jsonify(
        {
            'code': 200,
                'data': stock_detail.json()

        }
    )

if __name__ == '__main__':
    print("stock ")
    app.run(host='0.0.0.0', port=5001, debug=True)