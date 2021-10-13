from PharmaWeb.models.FormaFarmaceutica import FormaFamaceutica
from rest_framework import serializers

class FormaFamaceuticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaFamaceutica
        fields = '__all__'