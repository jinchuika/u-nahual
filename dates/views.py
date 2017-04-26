from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Nahual
from .serializers import NahualSerializer



class NahualListView(APIView):
	def get(self, request):
		nahuales = Nahual.objects.all()
		serializer = NahualSerializer(nahuales, many=True)
		return Response(serializer.data)
