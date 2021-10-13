from rest_framework.response import Response
from PharmaWeb.serializers.EntidadesSerializer import EntidadesSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view
from PharmaWeb.models import Entidades
@api_view(['GET', 'POST'])
def entidad_api_view(request):
    if request.method == 'GET':
        entidades = Entidades.objects.all()
        entidades_serializer = EntidadesSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = EntidadesSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def entidad_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = Entidades.objects.filter(id_Entidad=pk).first()
        entidades_serializer = EntidadesSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = Entidades.objects.filter(id_Entidad=pk).first()
        entidades_serializer = EntidadesSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = Entidades.objects.filter(id_Entidad=pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')
