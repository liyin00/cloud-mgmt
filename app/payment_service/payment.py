import os
from flask import Flask, redirect, request
from os import environ
import stripe
from dotenv import load_dotenv
load_dotenv()

# This is a public sample test API key.
# Don’t submit any personally identifiable information in requests made with this key.
# Sign in to see your own test API key embedded in code samples.
stripe.api_key = os.getenv('apikey') or environ.get("apikey")
app = Flask(__name__,
            static_url_path='',
            static_folder='public')

YOUR_DOMAIN = 'http://localhost:4242'

@app.route('/hello', methods=['GET'])
def hello():
    return "app created"
    
@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    try:
        data = request.get_json()
        total = float(data['price']) * int(data['quantity'])
        ## see what we want 
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    
                    #'price': '{{PRICE_ID}}',
                    'price' : data['price'],
                    'quantity': data['quantity'],
                    'total' : str(total)
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html', #this should redirect to the cart page with success alert
            cancel_url=YOUR_DOMAIN + '/cancel.html', #this should redirect to checkout page with error alert
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

if __name__ == '__main__':
    app.run(port=4242)