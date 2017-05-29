from django.conf.urls import url, include
from chat.views import ChatView
from django.conf import settings

urlpatterns = [
	url(
		r'^'+settings.FB_APP_KEY+'/?$',
		ChatView.as_view())
]