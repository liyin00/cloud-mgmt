from google.cloud import pubsub_v1
from google.oauth2 import service_account

import os
from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
import requests
import json
from os import environ
import stripe
from dotenv import load_dotenv
load_dotenv()

#Stripe API
# stripe.api_key = os.getenv('apikey') or environ.get("apikey")
stripe.api_key = 'sk_test_51IX1pfEh2v7rRS8AcPlo5xnom5URyB0pGOpVahhgBjIUWLThrnp864myMWWOj4Hbr6hxVJaDBiRI657dnwFOshmS008gjCP4fb'

#file path
# os.chdir(os.path.dirname(os.path.realpath(__file__)))
# file_path = 'elegant-fort-344208-514b10873dd0.json'

#gcloud credentials
svc_account =  {
  "type": "service_account",
  "project_id": "elegant-fort-344208",
  "private_key_id": "514b10873dd011c5b25ecf6dbf80a53911ffe898",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDcb71YTgv1R76V\nu4BHXiQUoI1vII2O7iZbgkDCmn55AqAYS4OoqFv/iBCdMWdEu8DH6sClPmb3nr1v\np8pd40zASpMT4H1gjwMKSf4my+tBxtU9/RqNRAHO216E8IRXl+BIFEcdJKrW6tYT\nNMZO33V3J6KXJsLrWOdEFWZ+P0Zeo2FldzGJX7iTCf2juGNpl/u6WNqxDpi4fPvU\nGmoKmtGHnIBUuFSU566aIM9N9+10wM0+G8xlRQev6fsasRRXerUJPXvb9+UxoSs1\nLlT1hiH0I7x+/cMZe+ONvbQxk6AKULbTlCOVMsDCyBCkxbFNLJL6He1wW7Un9f59\n9RCzG0odAgMBAAECggEAUIzUV8xNOlf5IKXffjS8Yn04sX7nu27yvUWffH0P8hAv\niDEv7xV2aK3DxG0lG0ywaV0zAC8JWTq8Zmyd2ikRBsM5c2344qvfpIbdRDgHw4Vw\nrrIqXayYLIqkw1dQROHOpwgh5FhdxSMTDvmd7XxiZCQrmagkWfOmro5TYZallDbZ\n17O0DAn2bNuqU7Y1SuQQm0BnNKdJkwYQNPhF1I6nLAlWetigh3V1+sfMrdL4iDg0\nHsVeyyTQpULunOhHGtu/NKzsTvkNd3INaAbqm0YjmU1IIFWxeg+bv44x7hoyHVJz\n+Z1TLspvX26P7Ht6c9+TdtHA+hL/gbRTe3n1oir/UQKBgQDz91G+OZtBixZ17fZN\nCjyf0ADQFiIM2M6fiGP4zQUZqbOC7874jhq3mFDi/BxzZKf0LG59JX7bI71obgFf\nIaRCDzsn6LVzvfU6hasOq+avfuEPJLWUQ/N50VaE6bcQ9VxluWfO7Fxy7ooHkFmA\n8GMrijraqurPBH4dr96ORFDd1wKBgQDnT0zgkHvKYa5EzF9Ch/a1gON+/Bbasn0G\nRjv+FLOnE5FOa84r1f2x8r3tXxLeINnRK2b0KpHWwAuxP8pN09h6wRhWpSqfHQvi\nCii5lgaYOHKCcqKkbMLNi40YqGkmMstW6rJJf4OrfqkGsgoyKk8el6PgkttlQSUg\nTgIk6rNRKwKBgQDl/sr5YqWTbOSH2QbSKkxs/VNG2RbQtbRVged9rwqX3vx0/E9K\n0+0sGFRpKPRJdSNBdoHTSX4GafMueEaiwLxx6poCTciCjRqbSViyRCz+Vccm15y3\nYjgvJ8NBGnSTcDzjSZ8r3HhrgaZu6w72F6nmajKB44/qCno60ool5RG3kQKBgHPk\no5wQSDXKY0pNK51mChI+lb1WCQ1iSIoQPpa7QJgBkdg843vLJ+U0vjxkWku5IelP\nWbIUciWq6zDPyUjdT6WRgeRHtOcr4nxKosT5iixSe+0oCp1fcOsTdIpaNvTQllji\nFpoErbALMh0Mr1cbI7EsQQuQCSTeUv+wlhpxDY8pAoGBAK6rovHke9AldWx8TgEb\nM48J2rz3odWfYaeESjk6cb3hxxn4RT6iK9pwZUT03EeVesl5CU1GqhfokYxnMIcx\nYiDn7gg9rbYlHSrXqSzZGPmZ95DZBbkMjZQtZFOQnMnIQmyEYlVApZ5bOvpg1Okb\nxbQ5wSVSxbKfvtVQNeTnee5n\n-----END PRIVATE KEY-----\n",
  "client_email": "claeserviceaccount@elegant-fort-344208.iam.gserviceaccount.com",
  "client_id": "114151717133567707894",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/claeserviceaccount%40elegant-fort-344208.iam.gserviceaccount.com"
}


credentials = service_account.Credentials.from_service_account_info(svc_account)
#initialize publisher
publisher = pubsub_v1.PublisherClient(credentials = credentials)
topic_path = publisher.topic_path('elegant-fort-344208', 'orderfulfillment')


app = Flask(__name__)
CORS(app)

DOMAIN = 'http://clae.me/cart'
# DOMAIN = 'http://127.0.0.1:3000/cart'

@app.route("/")
def payment_up():
    return "payment is uppppppp"
    
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        data = request.get_json()

        line_items = []
        for item in data['cart']:
            stripe_item = {
                'price_data': {
                    'product': item['product_id'],
                    'currency': 'sgd',
                    'unit_amount': int(item['price'])*100   
                },
                'quantity': item['quantity']
            }
            line_items.append(stripe_item)
        # print(line_items)
        ## see what we want 
        checkout_session = stripe.checkout.Session.create(
            line_items = line_items,
            metadata = {"user_id": data['user_id']},
            mode = 'payment',
            success_url = DOMAIN + '?success=true', #this should redirect to the cart page with success alert
            cancel_url = DOMAIN + '?cancelled=true', #this should redirect to checkout page with error alert
        )

        # print(checkout_session)

        return jsonify(
            {
                'code': 200,
                'id': checkout_session.id
            }
        ), 200

    except Exception as e:
        print("error: ", e)
        return jsonify(
            {
                'code': 403,
                'error': str(e)
            }
        ), 403

@app.route('/webhook', methods=['POST'])
def payment_success_webhook():
    # event = request.get_json()

    endpoint_secret = 'whsec_ad18e558b7faad716af5021d51dfa8d695452fe3721778c914ec89a6c522826a'

    payload = request.get_data(as_text=True)
    sig_header = request.headers.get('Stripe-Signature')
    event = None

    try:
        event = stripe.Webhook.construct_event(
			payload, sig_header, endpoint_secret
		)

    except ValueError as e:
        # Invalid payload
        return 'Invalid payload', 400
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return 'Invalid signature', 400

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        user_id = event['data']['object']['metadata']['user_id']
        try :
            value = {
                "result": {
                    "user_id": user_id,
                    "product_list": []
                }
            }
            headers =  {"Content-Type":"application/json"}
            response = requests.post('http://34.142.147.70:5006/modify_cart', data=json.dumps(value), headers=headers)
            print(response)
        except Exception as e:
            print(e)

        session_id = event['data']['object']['id']
        print("session_id: ", session_id)
        line_items = stripe.checkout.Session.list_line_items(session_id, limit=100)
        # print(line_items)
        # print("line_items type: ", type(line_items))

        pass_data = {
            'data' : []
        }
        value_data = line_items
        print(value_data)
        for i in range (0, len(value_data['data'])):
            container_array = {
                'amount_subtotal' : value_data['data'][i]['amount_subtotal'],
                'amount_total' : value_data['data'][i]['amount_total'],
                'product' :  value_data['data'][i]['price']['product'],
                'quantity' : str(value_data['data'][i]['quantity']),
                'user_id': user_id
                }
            pass_data['data'].append(container_array)

        # print(pass_data)

    # Data must be a bytestring
        data = json.dumps(pass_data)
        data = data.encode("utf-8")
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data)
        print(future.result())

        print(f"Published messages to {topic_path}.")

    return jsonify(
        {
            'code': 200,
            'data': 'success!!'
        }
    ), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242, debug=True)