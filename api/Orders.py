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
app.config['SQLALCHEMY_DATABASE_URI'] = config('dbURL') or  environ.get("dbURL")
# app.config['SQLALCHEMY_DATABASE_URI'] = config('localURL') or environ.get('localURL')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_size': 100,
                                           'pool_recycle': 280}

db = SQLAlchemy(app)

CORS(app)

class Orders(db.Model):
    __tablename__ = "Orders"
    order_id = db.Column(db.String(500),primary_key=True, nullable=False)
    user_id = db.Column(db.String(500), nullable=False)
    products_purchased = db.Column(db.String(500), nullable=False)
    purchased_quantity = db.Column(db.String(500), nullable=False)
    sub_prices = db.Column(db.String(500), nullable=False)
    total_price = db.Column(db.String(500), nullable=False)
    billing_address = db.Column(db.String(500), nullable=False)
    payment_status = db.Column(db.String(500), nullable=False)
    datetime_purchased= db.Column(db.String(500), nullable=False) 

    def create_order(self):
        try:
            db.session.add(self)
            db.session.commit()
            return 200
        except Exception as e:
            return 502

    def array_conversion_purchased(self):
        
        comma = ","
        if comma in self.products_purchased:
            array = self.products_purchased.split(',')
        else:
            return [self.products_purchased]
        return array

    def array_conversion_quantity(self):
        
        comma = ","
        if comma in self.purchased_quantity:
            array = self.purchased_quantity.split(',')
        else:
            return [self.purchased_quantity]
        return array

    def json(self):
        array_products_purchased = self.array_conversion_purchased()
        array_purchased_quantity = self.array_conversion_quantity()

        print(array_products_purchased)
        print(array_purchased_quantity)


        order_detail = {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'products_purchased': array_products_purchased,
            'purchased_quantity': array_purchased_quantity,
            'sub_prices': self.sub_prices,
            'total_price': self.total_price,
            'billing_address': self.billing_address,
            'payment_status': self.payment_status,
            'datetime_purchased' : self.datetime_purchased
        }
        return order_detail


@app.route("/get_orders_by_user_id/<string:user_id>", methods=['GET'])
def get_orders_by_user_id(user_id):
    try:
        # data = request.get_json()
        # user_id = data['user_id']

        order_list = Orders.query.filter_by(user_id=user_id).all()

        if(len(order_list)):
            print("enter")

            return jsonify(
            {
                'code': 200,
                'results': [order.json() for order in order_list]
            })
        return jsonify(
        {
            'code': 404,
            'results': "no order found"
        })
        
    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "message": "An error occurred while getting the order. " + str(e)
            }
        ), 500

@app.route("/create_order", methods=['POST'])
def create_order():
    #insert into class record, update slot available, delete from registration
    try:
        #retrieve id 
        Order = Orders.query.order_by(Orders.order_id.desc()).first()
        print(Order.order_id)
        print("hold")
        order_id_number = Order.order_id[1:]
        print(order_id_number)
        order_id_number = int(order_id_number) + 1
        order_id_number = "o" + str(order_id_number)
        print("order id now is " , order_id_number)

        now = datetime.now()
        data = request.get_json()

        # Should immediately exit upon failing this line.....
        
        order_record = Orders(
            order_id= order_id_number,
            user_id=data['user_id'],
            products_purchased=data['products_purchased'],
            purchased_quantity=data['purchased_quantity'],
            sub_prices=data['sub_prices'],
            total_price=data['total_price'],
            billing_address=data['billing_address'],
            payment_status=data['payment_status'],
            datetime_purchased = str(now)
            
        )

        insert_code = order_record.create_order()

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
    print("stock ")
    app.run(host='0.0.0.0', port=5000, debug=True)