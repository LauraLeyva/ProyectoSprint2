from rest_framework import serializers
from PharmaWeb.models.consecutivos import Consecutivos
from PharmaWeb.models.entidades import Entidades
from PharmaWeb.serializers.EntidadesSerializer import EntidadesSerializer


class ConsecutivosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consecutivos
        fields = '__all__'
