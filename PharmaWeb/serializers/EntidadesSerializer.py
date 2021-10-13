from PharmaWeb.models.entidades import Entidades
from rest_framework import serializers

class EntidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidades
        fields = '__all__'