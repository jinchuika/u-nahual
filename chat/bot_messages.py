import json
import requests
from django.conf import settings

def post_facebook_message(fbid, received_message):
    post_message_url = 'https://graph.facebook.com/me/messages?access_token='+settings.FB_APP_KEY
    response_msg = json.dumps({"recipient": {'id': fbid}, 'message': {'text': received_message}})
    status = requests.post(post_message_url, headers={'Content-Type': 'application/json'}, data=response_msg)
    print(status.json())

def setup_persistant_menu():
    pass