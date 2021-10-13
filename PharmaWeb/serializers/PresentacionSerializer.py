from PharmaWeb.models.Presentacion import Presentacion
from rest_framework import serializers

class PresentacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presentacion
        fields = '__all__'