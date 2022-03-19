from google.cloud import firestore
from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse

db = firestore.Client()
app = Flask(__name__)
api = Api(app)

def abort_if_product_not_exist(product_id):
    products_ref = db.collection('Products')
    ref = products_ref.where(u'productid',u'==',product_id)
    if not ref:
        abort(404, message = "task {} doesnt exist".format(product_id))


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('description')
parser.add_argument('price')_