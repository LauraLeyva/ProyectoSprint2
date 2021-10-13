from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from PharmaWeb.serializers.medicamentosSerializer import MedicamentosSerializer

from rest_framework.decorators import api_view
from PharmaWeb.models import Medicamentos
@api_view(['GET', 'POST'])
def Medicamentos_api_view(request):
    if request.method == 'GET':
        entidades = Medicamentos.objects.all()
        entidades_serializer = MedicamentosSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = MedicamentosSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def Medicamentos_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = Medicamentos.objects.filter(id_Medicamento = pk).first()
        entidades_serializer = MedicamentosSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = Medicamentos.objects.filter(id_Medicamentos = pk).first()
        entidades_serializer = MedicamentosSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = Medicamentos.objects.filter(id_Medicamentos = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')
