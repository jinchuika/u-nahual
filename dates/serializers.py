from rest_framework import serializers
from dates.models import Nahual


class NahualSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Nahual
        fields = '__all__'
