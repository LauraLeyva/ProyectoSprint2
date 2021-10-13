from PharmaWeb.models.Formula_Encabezado import FormulaEncabezado
from rest_framework import serializers

class FormulaEncabezadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormulaEncabezado
        fields = '__all__'