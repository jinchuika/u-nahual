from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from dates import views
from . import settings
from django.views import static

urlpatterns = [
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', admin.site.urls),
    url(r'^nahuales/numero/$', views.NumeroAPIView.as_view(), name='numero_api'),
    url(r'^nahuales/$', views.NahualAPIView.as_view(), name='nahual_api'),
    url(r'^nahuales/(?P<slug>[-\w]+)/$', views.NahualRetrieveView.as_view(), name='nahual_api_detail'),
    url(r'^nahual/(?P<slug>[-\w]+)', views.NahualDetailView.as_view(), name='nahual_detail'),
    url(r'^$', views.HomeView.as_view(), name='home'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
