from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
from google.oauth2 import service_account
import requests

import json
# TODO(developer)
# project_id = "your-project-id"
# subscription_id = "your-subscription-id"
# Number of seconds the subscriber should listen for messages
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

timeout = 5.0
credentials = service_account.Credentials.from_service_account_info(svc_account)


subscriber = pubsub_v1.SubscriberClient(credentials = credentials)
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_id}`
subscription_path = subscriber.subscription_path('elegant-fort-344208', 'ordersuccess')
#subscription_path2 = subscriber.subscription_path('linen-age-337916', 'test123123-sub-stock')


def callback(message: pubsub_v1.subscriber.message.Message) -> None:

    data = message.data.decode("utf-8")
    value = json.loads(data)
    print("-----------------------")
    # print(data)
    print(type(value))


    # print(value['project_id'])
    print("-----------------------")
    try :
        print('value value is ' , value)
        headers =  {"Content-Type":"application/json"}
        ###need to change to elastic IP
        response = requests.post('http://127.0.0.1:5000/create_order', data=json.dumps(value), headers=headers)
        print(response)
    except Exception as e:
        print(e)

    message.ack()


    

streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
#streaming_pull_future = subscriber.subscribe(subscription_path2, callback=callback2)
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
        