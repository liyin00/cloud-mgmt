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
        "type": "service_account",
        "project_id": "elegant-fort-344208",
        "private_key_id": "8b484a00d77396a82c74551a181090526741569c",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCJzircP6r2wYEG\nZ0oiB53Za6GS4aVoItkx00cDLyJjx3uD3BmUzwkLgSaeUSsw8kXKzD5VeT/lqQaA\nCK3NaEuaTDAh9z8+1/jzODo46F+RyLrrgvdEi9hpHUsgZyqqmGnzqDETGOjZHrmd\nVAL4YczUbPgwyaN8OfB1HaCuDyrQbnPSnsER7VqdrpH9vxvVue3TVTTX1BQ62pnP\nN7muGLv0PO77KHNiERg4ghgYhDjTfO0O9HdH+djQtE4DDSddBurQqilkxH/tq5HY\nYmrGOHvAaG1HYFAw070EiWDnuo4Afgjx/EokkL7vYoDXSTFWkaZHAAEshf3wijPK\nlGQUrJErAgMBAAECggEABsf/cfEsH5JsH/2LN1t6mA1k2Q6DjjlQyNPlxbFXFuPl\nHxsAo0MA5fEIDnheEL2LU6xzUM9zpoCH0lsa+mWser5PDAzXrub/2DAnJU/CDDF9\niUNbmaLsFlgbr0+EWPrBE/1t1MvAAZcyeRx+POzLIJTwLa5ufhl3zLuVgZs7dyA1\n0i5M5XIiPw6mDq4+Q6Qi7VO/GTOuiXpRUQ3MEy40Px12+W1N70G3G9xXZqGEwknB\nQp62xD6AUxOr34QNv9TvI5mKJg/HInfSZTSz4HCwdsoBDtgScy6U7oIgxByiWOlq\ndbFKtqX4m4qLwChxRvO/JXAbv+ytifKIlVHzMN/A8QKBgQDB5qAK3uFcSeJaSlmx\nTkuAV6ZDbBSu2yE0jC/REJY3cHzq9oUF9TwGgVZhXwx66VknlwLNli8jtOsxwlrk\nHhLdEi446Qmfcp12iXtFUfuhnPnn4P/4WOBeAFNFys1RL/gfYeKCuGZpGdTuZta6\nk7rYUFE9uHWJkseGhXN9On6dOQKBgQC18G47+X57z8whDSahjGaGIis31by3we25\nIwgi9hNaGbi0pZk89XkJ+E5NeBCtBaTMqY72iZq3hf8DZFf8m2Bo1Gshfgmve9oz\n/j7GbM95anCEie2drXrdEIKviMWrgY8XRu6kvP/EcvN4+1i11jSz/eLSX8nZXf4r\nao2w41AFgwKBgQCh7sUBzxlORbXvyeAWH1kWmhyUehLb5M1aYSkd5EhPjHYGlFKL\noz66ABHvx71YeMCoO4lvwFkl7NXu/G2DzUnbrm9Dv/r1Wnb+o9p7DfikA8EBUfrz\noOXgG01wH+pQP0tsigbtPKrqY1RctS3nK7EDLjBq5z3h4t8XDSRiFRPgoQKBgHXJ\nHdR+BUCqmoCbPvM/LfCQlmIjYXWlev1sjIv1uzmNhWKOAtLQKHgn5KmKnWEmUjad\nXwyEsUE24o2TnNLQ1G2Jd4HLUwHksLMQWhujvf3gxs9HbCm0ceJEGhcB+Na7naN4\nLG9CXGMV+EHOlvPBpYURTJLdqJOsoiwBY5Gs19V5AoGASyYDQzJWa+evtwjXw3n0\nPCeqfJUjSTRKBOYRsubGG6UM3+2aQSSEpoLxzBm3JLP6qxmTEuV0IJ1/ybuK3YVf\n4LBw3kZyX2bfhJ8UF7jnbPU7IAxsoY5L14n10nO+Y7lJ3sS8A3SnKSBkOWzUIZKe\nDk12b/QZ3b/tlZ/NcqnjIhI=\n-----END PRIVATE KEY-----\n",
        "client_email": "claeserviceaccount@elegant-fort-344208.iam.gserviceaccount.com",
        "client_id": "114151717133567707894",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/claeserviceaccount%40elegant-fort-344208.iam.gserviceaccount.com"
        }
    

cred = credentials.Certificate(service_account_info)
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
collection = db.collection('Cart')  # opens 'places' collection

# def service_acc_conversion():
    # service_account_info = {"credential":{
    #     "type": "service_account",
    #     "project_id": "elegant-fort-344208",
    #     "private_key_id": "8b484a00d77396a82c74551a181090526741569c",
    #     "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCJzircP6r2wYEG\nZ0oiB53Za6GS4aVoItkx00cDLyJjx3uD3BmUzwkLgSaeUSsw8kXKzD5VeT/lqQaA\nCK3NaEuaTDAh9z8+1/jzODo46F+RyLrrgvdEi9hpHUsgZyqqmGnzqDETGOjZHrmd\nVAL4YczUbPgwyaN8OfB1HaCuDyrQbnPSnsER7VqdrpH9vxvVue3TVTTX1BQ62pnP\nN7muGLv0PO77KHNiERg4ghgYhDjTfO0O9HdH+djQtE4DDSddBurQqilkxH/tq5HY\nYmrGOHvAaG1HYFAw070EiWDnuo4Afgjx/EokkL7vYoDXSTFWkaZHAAEshf3wijPK\nlGQUrJErAgMBAAECggEABsf/cfEsH5JsH/2LN1t6mA1k2Q6DjjlQyNPlxbFXFuPl\nHxsAo0MA5fEIDnheEL2LU6xzUM9zpoCH0lsa+mWser5PDAzXrub/2DAnJU/CDDF9\niUNbmaLsFlgbr0+EWPrBE/1t1MvAAZcyeRx+POzLIJTwLa5ufhl3zLuVgZs7dyA1\n0i5M5XIiPw6mDq4+Q6Qi7VO/GTOuiXpRUQ3MEy40Px12+W1N70G3G9xXZqGEwknB\nQp62xD6AUxOr34QNv9TvI5mKJg/HInfSZTSz4HCwdsoBDtgScy6U7oIgxByiWOlq\ndbFKtqX4m4qLwChxRvO/JXAbv+ytifKIlVHzMN/A8QKBgQDB5qAK3uFcSeJaSlmx\nTkuAV6ZDbBSu2yE0jC/REJY3cHzq9oUF9TwGgVZhXwx66VknlwLNli8jtOsxwlrk\nHhLdEi446Qmfcp12iXtFUfuhnPnn4P/4WOBeAFNFys1RL/gfYeKCuGZpGdTuZta6\nk7rYUFE9uHWJkseGhXN9On6dOQKBgQC18G47+X57z8whDSahjGaGIis31by3we25\nIwgi9hNaGbi0pZk89XkJ+E5NeBCtBaTMqY72iZq3hf8DZFf8m2Bo1Gshfgmve9oz\n/j7GbM95anCEie2drXrdEIKviMWrgY8XRu6kvP/EcvN4+1i11jSz/eLSX8nZXf4r\nao2w41AFgwKBgQCh7sUBzxlORbXvyeAWH1kWmhyUehLb5M1aYSkd5EhPjHYGlFKL\noz66ABHvx71YeMCoO4lvwFkl7NXu/G2DzUnbrm9Dv/r1Wnb+o9p7DfikA8EBUfrz\noOXgG01wH+pQP0tsigbtPKrqY1RctS3nK7EDLjBq5z3h4t8XDSRiFRPgoQKBgHXJ\nHdR+BUCqmoCbPvM/LfCQlmIjYXWlev1sjIv1uzmNhWKOAtLQKHgn5KmKnWEmUjad\nXwyEsUE24o2TnNLQ1G2Jd4HLUwHksLMQWhujvf3gxs9HbCm0ceJEGhcB+Na7naN4\nLG9CXGMV+EHOlvPBpYURTJLdqJOsoiwBY5Gs19V5AoGASyYDQzJWa+evtwjXw3n0\nPCeqfJUjSTRKBOYRsubGG6UM3+2aQSSEpoLxzBm3JLP6qxmTEuV0IJ1/ybuK3YVf\n4LBw3kZyX2bfhJ8UF7jnbPU7IAxsoY5L14n10nO+Y7lJ3sS8A3SnKSBkOWzUIZKe\nDk12b/QZ3b/tlZ/NcqnjIhI=\n-----END PRIVATE KEY-----\n",
    #     "client_email": "claeserviceaccount@elegant-fort-344208.iam.gserviceaccount.com",
    #     "client_id": "114151717133567707894",
    #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #     "token_uri": "https://oauth2.googleapis.com/token",
    #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/claeserviceaccount%40elegant-fort-344208.iam.gserviceaccount.com"
    #     }
    # }
#     os.chdir(os.path.dirname(os.path.realpath(__file__)))
#     config_path = 'elegant-fort-344208-514b10873dd0.json'
#     service_account_info = json.load(open(config_path))
#     return service_account_info

# # def service_acc_conversion():
# #     service_account_info = {"credential":
# #     {
# #         "type" :os.getenv("TYPE"),
# #         "project_id" : os.getenv("PROJECT_ID"),
# #         "private_key_id" : os.getenv("PRIVATE_KEY_ID"),
# #         "private_key" : os.getenv("PRIVATE_KEY").replace('\\n','\n'),
# #         "client_email" : os.getenv("CLIENT_EMAIL"),
# #         "client_id" : os.getenv("CLIENT_ID"),
# #         "auth_uri" : os.getenv("AUTH_URI"),
# #         "token_uri" : os.getenv("TOKEN_URI"),
# #         "auth_provider_x509_cert_url" : os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
# #         "client_x509_cert_url" : os.getenv("CLIENT_X509_CERT_URL")
# #     }}
# #     return service_account_info

# service_info = service_acc_conversion()
# cred = credentials.Certificate(service_info)
# default_app = firebase_admin.initialize_app(cred)
# print("-====")
# print(default_app)
# db = firestore.client()
# # print(db)
# collection = db.collection('Cart')  # opens 'places' collection
# doc = collection.document('59cgz68KGf1sF4Gz4Ilt')
# res = doc.get().to_dict()
# print(res)
# print("-----------")
# docs = todo_ref.get()
# print(docs)

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
