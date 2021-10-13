from PharmaWeb.models.Genericos import Genericos
from rest_framework import serializers

class GenericosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genericos
        fields = '__all__'