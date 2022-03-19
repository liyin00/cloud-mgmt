import firebase_admin

from firebase_admin import credentials, firestore
cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)


db = firestore.client()  # this connects to our Firestore database
collection = db.collection('product')  # opens 'places' collection
doc = collection.document('rome')  # specifies the 'rome' document

