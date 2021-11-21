from PharmaWeb.models.Medicamentos import Medicamentos
from rest_framework import serializers
from PharmaWeb.models.Laboratorios import Laboratorios
from PharmaWeb.serializers.LaboratoriosSerializer import LaboratoriosSerializer

class MedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamentos
        fields = '__all__'