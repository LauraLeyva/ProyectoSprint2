from PharmaWeb.models.Formula_Detalle import FormulaDetalle
from rest_framework import serializers

class FormulaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormulaDetalle
        fields = '__all__'