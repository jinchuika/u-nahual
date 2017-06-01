from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from dates import views
from django.conf import settings
from django.views import static

urlpatterns = [
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^nahual-admin/', admin.site.urls),
    url(r'^nahuales/numero/$', views.NumeroAPIView.as_view(), name='numero_api'),
    url(r'^nahuales/$', views.NahualAPIView.as_view(), name='nahual_api'),
    url(r'^nahuales/(?P<slug>[-\w]+)/$', views.NahualRetrieveView.as_view(), name='nahual_api_detail'),
    url(r'^nahual/(?P<slug>[-\w]+)/$', views.NahualDetailView.as_view(), name='nahual_detail'),
    url(r'^fecha/$', views.DateApiView.as_view(), name='fecha_api_view'),
    url(r'^$', views.HomeView.as_view(), name='home'),

    url(r'^chat/', include('chat.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
