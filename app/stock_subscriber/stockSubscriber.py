from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
from google.oauth2 import service_account
import requests

import json
# TODO(developer)
# project_id = "your-project-id"
# subscription_id = "your-subscription-id"
# Number of seconds the subscriber should listen for messages
timeout = 5.0
DOMAIN = '34.142.141.221'

svc_account =  {
# service account information
}

credentials = service_account.Credentials.from_service_account_info(svc_account)


subscriber = pubsub_v1.SubscriberClient(credentials = credentials)
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_id}`
subscription_path = subscriber.subscription_path('elegant-fort-344208', 'stocksuccess')
#subscription_path2 = subscriber.subscription_path('linen-age-337916', 'test123123-sub-stock')


def callback(message: pubsub_v1.subscriber.message.Message) -> None:

    data = message.data.decode("utf-8")
    value = json.loads(data)
    print("-----------------------")
    # print(data)
    print(type(value))

    try :

        headers =  {"Content-Type":"application/json"}
        response = requests.post(f'http://{DOMAIN}:5001/update_deduct_stock_by_product_id', data=json.dumps(value), headers=headers)
        print(response)
    except Exception as e:
        print(e)

    message.ack()


    

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
print(f"Listening for messages on {subscription_path}..\n")

# Wrap subscriber in a 'with' block to automatically call close() when done.
with subscriber:
    try:
        # When `timeout` is not set, result() will block indefinitely,
        # unless an exception is encountered first.
        streaming_pull_future.result()
    except TimeoutError:
        streaming_pull_future.cancel()  # Trigger the shutdown.
        streaming_pull_future.result()  # Block until the shutdown is complete.
        