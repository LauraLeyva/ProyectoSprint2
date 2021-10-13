from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from PharmaWeb.models.Formula_Encabezado import FormulaEncabezado
from PharmaWeb.serializers import formulaencabezadoSerializer

from PharmaWeb.serializers.formulaencabezadoSerializer import FormulaEncabezadoSerializer


from rest_framework.decorators import api_view
from PharmaWeb.models import FormulaEncabezado
@api_view(['GET', 'POST'])
def FormulaEncabezado_api_view(request):
    if request.method == 'GET':
        entidades = FormulaEncabezado.objects.all()
        entidades_serializer = FormulaEncabezadoSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = FormulaEncabezadoSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def FormulaEncabezado_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = FormulaEncabezado.objects.filter(id_Formula_Encabezado = pk).first()
        entidades_serializer = FormulaEncabezadoSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = FormulaEncabezado.objects.filter(id_Formula_Encabezado = pk).first()
        entidades_serializer = FormulaEncabezadoSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = FormulaEncabezado.objects.filter(id_Formula_Encabezado = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')
