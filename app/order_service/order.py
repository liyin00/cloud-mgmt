# Might change this to using os.environ.get() instead in future sprints
# from decouple import config
from flask import Flask, json, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()

# from classes import *

# Database connection

# EC2 DB port is 3306 instead, change accordingly.
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql+pymysql://$user:$password@$db_ip:$port/$databasename"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True

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
    payment_status = db.Column(db.String(1), nullable=False)
    order_status = db.Column(db.String(500), nullable=False)
    datetime_purchased= db.Column(db.String(500), nullable=False) 

    def create_order(self):
        try:
            print("self is")
            print(self)
            db.session.add(self)
            db.session.commit()
            return 200
        except Exception as e:
            #change value
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
            'order_status': self.order_status,
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
        print("test")
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
        data = data['data']
        amount_subtotal = 0
        amount_total = 0 
        product = ''
        quantity = ''
        ###compute area #####

        for i in range(0, len(data)):
            print("------------------------")
            print(data[i]['amount_subtotal'])
            print(data[i]['amount_total'])
            print(data[i]['product'] )
            print(data[i]['quantity'])
            print("------------------------")

            amount_subtotal +=  data[i]['amount_subtotal']
            amount_total += data[i]['amount_total']
            product =  data[i]['product'] + ","  + product
            quantity = str(data[i]['quantity'])  + ","  + quantity
            user_id = data[i]['user_id']

            
 

        ###compute area #####
        # Should immediately exit upon failing this line.....
        
        order_record = Orders(
            order_id= order_id_number,
            user_id=user_id,
            products_purchased=product[:len(product)-1],
            purchased_quantity=quantity[:len(quantity)-1],
            sub_prices=amount_subtotal,
            total_price=amount_total,
            billing_address="Pasir Ris Ave 10 Block 123 560123",
            payment_status=1,
            order_status = "Pending",
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


@app.route("/get_order_list", methods=['GET'])
def get_order_list():
    try:
        # data = request.get_json()
        # user_id = data['user_id']

        order_list = Orders.query.filter_by().all()

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



@app.route("/update_order_status", methods=['PUT'])
def update_order_status():
    try:
        data = request.get_json()
        order_id = data['order_id']
        order_status = data['order_status']

        order = Orders.query.filter_by(order_id=order_id).first()
        if not order:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "order_id": order_id
                    },
                    "message": "order_id" + str(order_id) +  "not found."
                }
            ), 404
        order.order_status = order_status

        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": order.json(),
                "message": "successfully updated order"
            }
        ), 200



    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "order_id": order_id
                },
                "message": "An error occurred while updating the order status. " + str(e)
            }
        ), 500





@app.route("/update_payment_status", methods=['PUT'])
def update_payment_status():
    try:
        data = request.get_json()
        order_id = data['order_id']
        payment_status = data['payment_status']

        order = Orders.query.filter_by(order_id=order_id).first()
        if not order:
            return jsonify(
                {
                    "code": 404,
                    "data": {
                        "order_id": order_id
                    },
                    "message": "order_id" + str(order_id) +  "not found."
                }
            ), 404
        order.payment_status = payment_status

        db.session.commit()
        return jsonify(
            {
                "code": 200,
                "data": order.json(),
                "message": "successfully updated payment status "
            }
        ), 200



    except Exception as e:
        return jsonify(
            {
                "code": 500,
                "data": {
                    "order_id": order_id
                },
                "message": "An error occurred while updating the payment status. " + str(e)
            }
        ), 500


@app.route("/check", methods=['GET'])
def check():
        return jsonify(
            {
                'code': 200,
                'data': "order",
                'desc': "success"
                
            }
        )

if __name__ == '__main__':
    print("order ")
    app.run(host='0.0.0.0', port=5000, debug=True)