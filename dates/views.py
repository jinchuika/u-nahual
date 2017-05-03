from django.views.generic import FormView, DetailView

from rest_framework.generics import RetrieveAPIView

from .models import Nahual
from .forms import NahualBuscarForm
from .serializers import NahualSerializer
from datetime import date, datetime


class NahualAPIView(RetrieveAPIView):
    serializer_class = NahualSerializer

    def get_queryset(self):
        d0 = date(1900, 1, 1)
        dia = self.request.query_params.get('dia')
        mes = self.request.query_params.get('mes')
        anno = self.request.query_params.get('anno')
        try:
            d1 = date(
                int(self.request.query_params.get('anno')),
                int(self.request.query_params.get('mes')),
                int(self.request.query_params.get('dia')))
        except TypeError:
            d1 = datetime.now().date()
        except ValueError:
            d1 = datetime.now().date()
        delta = d1 - d0
        count = delta.days + 1
        nahual = count % 20
        return Nahual.objects.filter(id=nahual)

    def get_object(self):
        queryset = self.get_queryset()
        return queryset.first()


class HomeView(FormView):
    form_class = NahualBuscarForm
    template_name = 'index.html'

    def get_form(self, form_class=None):
        form = self.form_class(**self.get_form_kwargs())
        if self.request.GET.get('fecha', None):
            form.initial['fecha'] = self.request.GET.get('fecha', None)
        return form


class NahualDetailView(DetailView):
    model = Nahual
    template_name = 'nahual_detail.html'
    slug_url_kwarg = 'slug'
