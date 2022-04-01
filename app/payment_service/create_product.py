# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import os
from flask import Flask, redirect, request
from os import environ
from dotenv import load_dotenv
load_dotenv()
import stripe


stripe.api_key = os.getenv('apikey') or environ.get("apikey")

product_list = [
    {
        "data": {
            "is_active": 1, 
            "price": "10",
            "price_id": "price_1KhTw3Eh2v7rRS8AKJOYT36A",
            "product_description": "A crop tee suitable for any ages", 
            "product_img": " https://storage.cloud.google.com/is548_cloud_product_image/p1.png", 
            "product_name": "Solid Button Crop Tee", 
            "size": "S,M,L"
        }, 
        "product_id": "prod_LOGHr3LAjFzSeK"
    }, 
    {
        "data": {
            "is_active": 1, 
            "price": "21",
            "price_id": "price_1KhTw4Eh2v7rRS8AC25Q6Dxv",
            "product_description": "Blouse that only available in green. ", 
            "product_img": " https://storage.cloud.google.com/is548_cloud_product_image/p10.png", 
            "product_name": "DAZY Solid Puff Sleeve Blouse"
        }, 
        "product_id": "prod_LOGHBvyxc11Kgq"
    }, 
    {
        "data": {
            "colour": "beige,red,pink", 
            "is_active": 1, 
            "price": "13",
            "price_id": "price_1KhTw4Eh2v7rRS8A3xp707Tn",
            "product_description": "Tee with only 2 buttons with only 1 color available", 
            "product_img": " https://storage.cloud.google.com/is548_cloud_product_image/p2.png", 
            "product_name": "Contrast Trim Polo Neck Tee", 
            "size": "M,L"
        }, 
        "product_id": "prod_LOGHz1EAtZZg11"
    }, 
    {
        "data": {
            "colour": "beige,blue", 
            "is_active": 1, 
            "price": "22", 
            "price_id": "price_1KhTw4Eh2v7rRS8AIqvPgnUw",
            "product_description": "Pants suitable for all ages, with a very stylish fashion.", 
            "product_img": "https://storage.cloud.google.com/is548_cloud_product_image/p3.png", 
            "product_name": "High Waist Slant Pocket Pants"
        }, 
        "product_id": "prod_LOGHdglhHiOSSk"
    }, 
    {
        "data": {
            "is_active": 1, 
            "price": "28", 
            "price_id": "price_1KhTw5Eh2v7rRS8AMwnW7fYo",
            "product_description": "Dress with buttons.", 
            "product_img": "https://storage.cloud.google.com/is548_cloud_product_image/p4.png", 
            "product_name": "Button Up Ruched Waist Split Hem Shirt Dress"
        }, 
        "product_id": "prod_LOGHtD8zryYRw4"
    }, 
    {
        "data": {
            "is_active": 1, 
            "price": "23", 
            "price_id": "price_1KhTw5Eh2v7rRS8AxibmxqjI",
            "product_description": "Striped Dress that allows you to look tall in any event.", 
            "product_img": "https://storage.cloud.google.com/is548_cloud_product_image/p5.png", 
            "product_name": "Sollinarry Striped Ruched Shirt Dress", 
            "size": "XS,S,M"
        }, 
        "product_id": "prod_LOGHdYhhiivHH2"
    }, 
    {
        "data": {
            "is_active": 1, 
            "price": "12", 
            "price_id": "price_1KhTw6Eh2v7rRS8Av6gYqn82",
            "product_description": "A dress with inbuilt belt that allow you to showcase your fashion", 
            "product_img": "https://storage.cloud.google.com/is548_cloud_product_image/p6.png", 
            "product_name": "Sollinarry Ruched Batwing Sleeve Belted Shirt Dress", 
            "size": "XS,S"
        }, 
        "product_id": "prod_LOGHmsrfVUxCce"
    }, 
    {
        "data": {
            "is_active": 1, 
            "price": "4", 
            "price_id": "price_1KhTw6Eh2v7rRS8Ad6b630dg",
            "product_description": "A necklace that only available in 1 size", 
            "product_img": "https://storage.cloud.google.com/is548_cloud_product_image/p7.png", 
            "product_name": "Rhinestone & Heart Charm Layered Necklace"
        }, 
        "product_id": "prod_LOGHmlJ262z0v9"
    }, 
    {
        "data": {
            "is_active": 1, 
            "price": "12", 
            "price_id": "price_1KhTw7Eh2v7rRS8ApuJkrHtk",
            "product_description": "V-neck blouse that will reveal your collar bone", 
            "product_img": "https://storage.cloud.google.com/is548_cloud_product_image/p8.png", 
            "product_name": "DAZY Contrast Lace V-neck Puff Sleeve Blouse"
        }, 
        "product_id": "prod_LOGH1MCR4Dk5vq"
    }, 
    {
        "data": {
            "is_active": 1, 
            "price": "20", 
            "price_id": "price_1KhTw7Eh2v7rRS8At68JMoZ0",
            "product_description": "Blouse that only available in 1 sizing and 1 colour", 
            "product_img": "https://storage.cloud.google.com/is548_cloud_product_image/p9.png", 
            "product_name": "DAZY Top-stitching Puff Sleeve Blouse"
        }, 
        "product_id": "prod_LOGHNcHLMP7T0o"
    }
]

#create products
# product_id_list = []
# for product in product_list:
#     product_name = product['data']['product_name']
#     product_id = product['product_id']

#     stripe_product = stripe.Product.create(name=product_name)
#     product_id_list.append(stripe_product['id'])

# print(product_id_list)

# pid = 'prod_LOGHr3LAjFzSeK'

# stripe_price = stripe.Price.create(
#     product=pid,
#     unit_amount=1000,
#     currency="sgd",
# )

# print(stripe_price)

#create price_id
# product_price_list = []
# for product in product_list:
#     product_id = product['product_id']
#     product_price = product['data']['price']

#     stripe_price = stripe.Price.create(
#         product=product_id,
#         unit_amount=int(product_price)*100,
#         currency="sgd",
#     )

#     product_price_list.append(stripe_price['id'])

# print(product_price_list)

# for product in product_list:
#     product_id = product['product_id']
#     product_img = "https:" + product['data']['product_img'].split(":")[1]

#     stripe.Product.modify(
#         product_id,
#         images=[product_img]
#     )