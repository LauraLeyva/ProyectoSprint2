from PharmaWeb.models.Sistema_Organico import Sistema_Organico
from rest_framework import serializers

class Sistema_OrganicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sistema_Organico
        fields = '__all__'