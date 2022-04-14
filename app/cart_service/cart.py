# app.py

# Required imports
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from os import environ
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
load_dotenv()
import json
import os
# Initialize Flask app
app = Flask(__name__)
CORS(app)

service_account_info = {
    # firebase_service_account
    }

cred = credentials.Certificate(service_account_info)
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
collection = db.collection('Cart')  # opens 'places' collection

#when select a item and add them to cart because usually is add 1 by 1  (when making specifc item)
@app.route("/create_cart_item", methods=['POST'])
def create_cart_item():
    #check the document if the user exist if not then create 
    try:
        data = request.get_json()
        user_id = data['user_id']
        # print(data)
        # print(data['user_id'])
        doc = collection.document(user_id).get()
        # print(doc)
        del data["user_id"]
        if(doc.exists):
            print("exist")
            print(doc.id)
            print(doc.to_dict()['product_list'])
            # print(doc.data()['product_list'])
            # value = doc.to_dict()['product_list']
            print("below")
            # print(value)  
            print(data)
            is_already_exist_product = 0 
            #check if product exist inside document 
            value = list(doc.to_dict()['product_list'])
            print("product id now is " + data['product_id'])
            print("length of the product list currently is " + str(len(value)))

            for i in range(0,len(value)):
                print("product_id current is " + value[i]['product_id'])
                if (data['product_id'] == value[i]['product_id']):
                    total = int(value[i]['quantity']) + 1
                    value[i]['quantity'] = str(total)
                    is_already_exist_product = 1

            #means is new item 
            if(is_already_exist_product == 0):
                value.append(data)
                print(value)

            res = collection.document(user_id).update({
                'product_list': value
                })

        else:
            print("new")
            res = collection.document(user_id).set({
                'user_id' : user_id,
                'product_list': [data]
            }
            )



        return jsonify(
            {
                'code': 200,
                'data': {},
                'desc': "success"

            }
        )
        
    except Exception as e:
        return jsonify(
            {
                'code': 500,
                'data': {},
                'desc': "An Error Occured:" + str(e)

            }
        )


@app.route("/get_cart_by_user_id/<string:user_id>", methods=['GET'])
def get_cart_by_user_id(user_id):
    try:
        doc = collection.document(user_id)
        res = doc.get().to_dict()
        return jsonify(
            {
                'code': 200,
                'data': res,
                'desc': "success"
                
            }
        )
    except Exception as e:
        return jsonify(
            {
                'code': 500,
                'data': {},
                'desc': "An Error Occured:" + str(e)
                
            }
        )

@app.route("/modify_cart", methods=['POST'])
def modify_cart():
    try:
        #if the user delete all the cart item, should not be a problem because product_list will be []
        #means the user cart exist BUT, it is deem as exist but is empty instead
        print("enter modify cart")

        data = request.get_json()
        print(data)
        data = data['result']
        print(data)
        user_id = data['user_id']
        product_list = data['product_list']

        doc = collection.document(user_id).get()
        del data["user_id"]
        array  = []
        # product_id = data['product_id'].split(",")
        # print(product_id)
        # price = data['price'].split(",")
        # quantity = data['quantity'].split(",")
        # product_name = data['product_name'].split(",")
        # product_description = data['product_description'].split(",")
        # product_img = data['product_img'].split(",")
        
        if(len(data['product_list']) == 0):
            #delete the document 
            print("no more should delete")
            collection.document(user_id).delete()
        else:
            print("got existing data")
            res = collection.document(user_id).update({
                'product_list': product_list
                })

        return jsonify(
            {
                'code': 200,
                'data': {},
                'desc': "success"

            }
        )
    
    
    except Exception as e:
        return jsonify(
            {
                'code': 500,
                'data': {},
                'desc': "An Error Occured:" + str(e)

            }
        )




# @app.route("/modify_cart", methods=['POST'])
# def modify_cart():
#     try:
#         #if the user delete all the cart item, should not be a problem because product_list will be []
#         #means the user cart exist BUT, it is deem as exist but is empty instead

#         data = request.get_json()
#         user_id = data['user_id']

#         doc = collection.document(user_id).get()
#         del data["user_id"]
#         array  = []
#         product_id = data['product_id'].split(",")
#         print(product_id)
#         price = data['price'].split(",")
#         quantity = data['quantity'].split(",")
#         product_name = data['product_name'].split(",")
#         product_description = data['product_description'].split(",")
#         product_img = data['product_img'].split(",")
        
#         print(len(product_id))
#         if(product_id == ['']):
#             #delete the document 
#             collection.document(user_id).delete()
#         else:
#             for i in range(0, len(product_id)):
#                 value = {
#                     "product_id" : product_id[i],
#                     "price" : price[i],
#                     "quantity" : quantity[i],
#                     "product_name" : product_name[i],
#                     "product_description" : product_description[i],
#                     "product_img" : product_img[i],


#                 }
#                 array.append(value)

#         res = collection.document(user_id).update({
#             'product_list': array
#             })




#         return jsonify(
#             {
#                 'code': 200,
#                 'data': {},
#                 'desc': "success"

#             }
#         )
        

    
#     except Exception as e:
#         return jsonify(
#             {
#                 'code': 500,
#                 'data': {},
#                 'desc': "An Error Occured:" + str(e)

#             }
#         )

@app.route("/check", methods=['GET'])
def check():
        return jsonify(
            {
                'code': 200,
                'data': "cart",
                'desc': "success"
                
            }
        )




if __name__ == '__main__':
    print("cart ")
    app.run(host='0.0.0.0', port=5006, debug=True)
