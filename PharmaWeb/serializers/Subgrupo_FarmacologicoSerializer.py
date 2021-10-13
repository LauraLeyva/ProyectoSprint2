from PharmaWeb.models.Subgrupo_Farmacologico import Subgrupo_Farmacologico
from rest_framework import serializers

class Subgrupo_FarmacologicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgrupo_Farmacologico
        fields = '__all__'