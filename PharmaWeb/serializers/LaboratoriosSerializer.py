from PharmaWeb.models.Laboratorios import Laboratorios
from rest_framework import serializers

class LaboratoriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratorios
        fields = '__all__'
        