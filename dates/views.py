from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView

from .models import Nahual
from .serializers import NahualSerializer
from datetime import date


class NahualListView(ListAPIView):
    serializer_class = NahualSerializer

    def get_queryset(self):
        d0 = date(1900, 1, 1)
        d1 = date(
            int(self.request.query_params.get('anno')), 
            int(self.request.query_params.get('mes')), 
            int(self.request.query_params.get('dia')))
        delta = d1 - d0
        count = delta.days + 1
        nahual = count % 20
        return Nahual.objects.filter(id=nahual)
