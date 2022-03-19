# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import os
from flask import Flask, redirect, request
from os import environ
from decouple import config
import stripe


stripe.api_key = config('apikey') or  environ.get("apikey")

# value = stripe.Product.create(name="Mini Black Dress")
price_tagger = stripe.Price.create(
  product="prod_LIeiCRuSbRlaxD",
  unit_amount=2000,
  currency="sgd",
)
print(price_tagger)