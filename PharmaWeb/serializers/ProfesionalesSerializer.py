from PharmaWeb.models.Profesionales import Profesionales
from rest_framework import serializers

class ProfesionalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesionales
        fields = '__all__'