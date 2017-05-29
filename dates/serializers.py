from rest_framework import serializers
from dates.models import Nahual


class NahualSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='nahual_detail', lookup_field='slug')
    siguiente_fecha = serializers.CharField(source='get_siguiente_fecha', read_only=True)

    class Meta:
        model = Nahual
        fields = '__all__'
        lookup_field = 'slug'


class NumeroSerializer(serializers.Serializer):
    numero = serializers.IntegerField()


class FechaSerializer(serializers.Serializer):
	nahual = NahualSerializer()
	numero = NumeroSerializer()
		