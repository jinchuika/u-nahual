from datetime import date, datetime
from django.views.generic import FormView, DetailView

from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, GenericAPIView

from .models import Nahual
from .forms import NahualBuscarForm
from .serializers import NahualSerializer, NumeroSerializer, FechaSerializer


class NahualAPIView(RetrieveAPIView):
    serializer_class = NahualSerializer
    queryset = Nahual.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        d0 = date(1900, 1, 1)
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
        nahual_id = count % 20
        if nahual_id == 0:
            nahual_id = 20
        nahual = queryset.get(id=nahual_id)
        return nahual


class NumeroAPIView(RetrieveAPIView):
    serializer_class = NumeroSerializer
    queryset = []

    def get_queryset(self):
        d0 = date(1900, 1, 1)
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
        numero = 0
        numero_calc = (count % 13) + 3
        if numero_calc > 13:
            numero = numero_calc - 13
        elif numero_calc == 0:
            numero = 13
        else:
            numero = numero_calc
        return [{'numero': numero}]

    def get_object(self):
        queryset = self.get_queryset()
        return queryset[0]


class NahualRetrieveView(RetrieveAPIView):
    serializer_class = NahualSerializer
    queryset = Nahual.objects.all()
    lookup_field = 'slug'


class DateApiView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        d0 = date(1900, 1, 1)
        try:
            d1 = date(
                int(self.request.query_params.get('year')),
                int(self.request.query_params.get('month')),
                int(self.request.query_params.get('day')))
        except TypeError:
            d1 = datetime.now().date()
        except ValueError:
            d1 = datetime.now().date()
        delta = d1 - d0
        count = delta.days + 1
        nahual_id = count % 20
        if nahual_id == 0:
            nahual_id = 20
        nahual = Nahual.objects.get(id=nahual_id)
        numero = 0
        numero_calc = (count % 13) + 3
        if numero_calc > 13:
            numero = numero_calc - 13
        elif numero_calc == 0:
            numero = 13
        else:
            numero = numero_calc
        combinado = {'nahual': nahual, 'numero': {'numero': numero}}
        serializer = FechaSerializer(combinado, context={'request': request})
        return Response(serializer.data)


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
