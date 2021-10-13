from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from PharmaWeb.serializers.formuladetalleSerializer import FormulaDetalleSerializer

from rest_framework.decorators import api_view
from PharmaWeb.models import FormulaDetalle
@api_view(['GET', 'POST'])
def FormulaDetalle_api_view(request):
    if request.method == 'GET':
        entidades = FormulaDetalle.objects.all()
        entidades_serializer = FormulaDetalleSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = FormulaDetalleSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def FormulaDetalle_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = FormulaDetalle.objects.filter(id_Formula_Detalle = pk).first()
        entidades_serializer = FormulaDetalleSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = FormulaDetalle.objects.filter(id_Formula_Detalle = pk).first()
        entidades_serializer = FormulaDetalleSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = FormulaDetalle.objects.filter(id_Formula_Detalle = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')
