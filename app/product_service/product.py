# app.py

# Required imports
from  os import environ
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import os
import base64
from dotenv import load_dotenv
load_dotenv()
import json
from flask_cors import CORS

# Initialize Flask app 
app = Flask(__name__)
CORS(app)

# def service_acc_conversion():
#     service_account_info = {"credential":
#     {
#         "type" :os.getenv("TYPE"),
#         "project_id" : os.getenv("PROJECT_ID"),
#         "private_key_id" : os.getenv("PRIVATE_KEY_ID"),
#         "private_key" : os.getenv("PRIVATE_KEY").replace('\\n','\n'),
#         "client_email" : os.getenv("CLIENT_EMAIL"),
#         "client_id" : os.getenv("CLIENT_ID"),
#         "auth_uri" : os.getenv("AUTH_URI"),
#         "token_uri" : os.getenv("TOKEN_URI"),
#         "auth_provider_x509_cert_url" : os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
#         "client_x509_cert_url" : os.getenv("CLIENT_X509_CERT_URL")
#     }}
#     return service_account_info

# def service_acc_conversion():
#     service_account_info = {"credential":
#     {
#         "type" : "service_account",
#         "project_id" : "elegant-fort-344208",
#         "private_key_id" : os.getenv("PRIVATE_KEY_ID"),
#         "private_key" : os.getenv("PRIVATE_KEY").replace('\\n','\n'),
#         "client_email" : os.getenv("CLIENT_EMAIL"),
#         "client_id" : os.getenv("CLIENT_ID"),
#         "auth_uri" : os.getenv("AUTH_URI"),
#         "token_uri" : os.getenv("TOKEN_URI"),
#         "auth_provider_x509_cert_url" : os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
#         "client_x509_cert_url" : os.getenv("CLIENT_X509_CERT_URL")
#     }}
#     return service_account_info

def service_acc_conversion():
    service_account_info = {"credential":{
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
}
    return service_account_info

service_info = service_acc_conversion()
# print('service info is ' , service_info)
cred = credentials.Certificate(service_info)
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()
collection = db.collection('Products')  # opens 'places' collection

# for liveness probe 
@app.route("/", methods=['GET'])
def returnlive():
    return jsonify({
        'code': 200,
        'desc': "success"
    })

#testing
@app.route("/get_product_name/<string:product_name>", methods=['GET'])
def get_product_name(product_name):
    try:
        # doc = collection.where('product_name', '=', product_name).get()
        # collection = db.collection(u'Products')
        # query_ref = collection.where(u'product_name', u'==', product_name).get().stream()
        # print("here")
        # print(product_name)
        # print(query_ref)
        array = []
        
        docs = collection.where(u'product_name', u'==', product_name).stream()
        print("value is " , docs.id)
        for doc in docs:

            print(f'{doc.id} => {doc.to_dict()}')
            value = {
                "product_id" : doc.id,
                "data": doc.to_dict()
                

            }
            array.append(value)

        print("come")
        return jsonify(
            {
                'code': 200,
                'data': array,
                'desc': "success"
                
            }
        )
    except Exception as e:
        return jsonify(
            {
                'code': 500,
                'data': {},
                'desc': "An Error Occured: {e}"
                
            }
        )


# print(res)
@app.route("/get_product_by_id/<string:product_id>", methods=['GET'])
def get_specific_product(product_id):
    try:
        doc = collection.document(product_id)
        res = doc.get().to_dict()
        return jsonify(
            {
                'code': 200,
                'product_id' : product_id,
                'data': res,
                'desc': "success"
                
            }
        )
    except Exception as e:
        return jsonify(
            {
                'code': 500,
                'data': {},
                'desc': "An Error Occured: {e}"
                
            }
        )
    


@app.route('/get_product_list', methods=['GET'])
def get_product_list():
    try:
        collection = db.collection('Products') 
        docs = collection.get()
        array = [] 
        for doc in docs:

            print(f'{doc.id} => {doc.to_dict()}')
            value = {
                "product_id" : doc.id,
                "data": doc.to_dict()
                

            }
            array.append(value)


        return jsonify(
            {
                'code': 200,
                'data': array,
                'desc':"success"
                
            }
        )
    except Exception as e:
        return jsonify(
            {
                'code': 500,
                'data': {},
                'desc': "An Error occured: {e}"
                
            }
        )
    

## for developer to insert data 
@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body.
        Ensure you pass a custom ID as part of json body in post request,
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        res = collection.document('p10').set({
            'product_name': 'DAZY Solid Puff Sleeve Blouse', 
            'product_description' : 'Blouse that only available in green. ',
            'price' : '21',
            'product_img': ' https://storage.cloud.google.com/is548_cloud_product_image/p10.png',
            'is_active': 1
        })


        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"

# @app.route('/list', methods=['GET'])
# def read():
#     """
#         read() : Fetches documents from Firestore collection as JSON.
#         todo : Return document that matches query ID.
#         all_todos : Return all documents.
#     """
#     try:
#         # Check if ID was passed to URL query
#         todo_id = request.args.get('id')
#         if todo_id:
#             todo = todo_ref.document(todo_id).get()
#             return jsonify(todo.to_dict()), 200
#         else:
#             all_todos = [doc.to_dict() for doc in todo_ref.stream()]
#             return jsonify(all_todos), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"

# @app.route('/update', methods=['POST', 'PUT'])
# def update():
#     """
#         update() : Update document in Firestore collection with request body.
#         Ensure you pass a custom ID as part of json body in post request,
#         e.g. json={'id': '1', 'title': 'Write a blog post today'}
#     """
#     try:
#         id = request.json['id']
#         todo_ref.document(id).update(request.json)
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"

# @app.route('/delete', methods=['GET', 'DELETE'])
# def delete():
#     """
#         delete() : Delete a document from Firestore collection.
#     """
#     try:
#         # Check for ID in URL query
#         todo_id = request.args.get('id')
#         todo_ref.document(todo_id).delete()
#         return jsonify({"success": True}), 200
#     except Exception as e:
#         return f"An Error Occured: {e}"

# port = int(os.environ.get('PORT', 8080))
# if __name__ == '__main__':
#     app.run(threaded=True, host='0.0.0.0', port=port)

@app.route("/check", methods=['GET'])
def check():
        return jsonify(
            {
                'code': 200,
                'data': "product",
                'desc': "success"
                
            }
        )

if __name__ == '__main__':
    print("order ")
    app.run(host='0.0.0.0', port=5005, debug=True)