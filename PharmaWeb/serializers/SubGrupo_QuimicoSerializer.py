from PharmaWeb.models.Subgrupo_Quimico import Subgrupo_Quimico
from rest_framework import serializers

class Subgrupo_QuimicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgrupo_Quimico
        fields = '__all__'