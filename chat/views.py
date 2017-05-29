from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views import generic
from django.http.response import HttpResponse

from chat.bot_messages import *


@method_decorator(csrf_exempt, name='dispatch')
class ChatView(generic.View):

    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '321654987':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalida token')

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        for entry in incoming_message['entry']:
            for message in entry['messaging']:
                if 'message' in message:
                    post_facebook_message(message['sender']['id'], message['message']['text'])
        return HttpResponse()
        
