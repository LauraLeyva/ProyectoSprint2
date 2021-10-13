from PharmaWeb.models.Grupo_Farmacologico import Grupo_Farmacologico
from rest_framework import serializers

class Grupo_FarmacologicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo_Farmacologico
        fields = '__all__'