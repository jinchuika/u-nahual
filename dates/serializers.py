from rest_framework import serializers
from dates.models import Nahual


class NahualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nahual
        fields = '__all__'
