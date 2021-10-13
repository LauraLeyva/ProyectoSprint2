from PharmaWeb.models.Medicamentos import Medicamentos
from rest_framework import serializers

class MedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamentos
        fields = '__all__'