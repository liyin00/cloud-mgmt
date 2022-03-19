# app.py

# Required imports
from  os import environ
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import os

from dotenv import load_dotenv
load_dotenv()
import json

# Initialize Flask app 
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate(json.loads(environ.get("SERVICE_ACC")))
default_app = firebase_admin.initialize_app(cred)
print("-====")
print(default_app)
db = firestore.client()
# print(db)
collection = db.collection('Products')  # opens 'places' collection
# doc = collection.document('59cgz68KGf1sF4Gz4Ilt') 
# res = doc.get().to_dict()
# print(res)
# print("-----------")
# docs = todo_ref.get()
# print(docs)

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
            'product_price' : '21',
            'product_img': '',
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

if __name__ == '__main__':
    print("order ")
    app.run(host='0.0.0.0', port=5005, debug=True)