from django.db import models
from PharmaWeb.models.entidades import Entidades


class Consecutivos(models.Model):
    id_Consecutivo = models.AutoField(primary_key=True)
    Numero_Inicial= models.IntegerField('Numero_Inicial')
    Numero_Final= models.IntegerField('Numero_Final')
    id_Entidad=models.ForeignKey(Entidades,related_name='Consecutivos', on_delete=models.CASCADE)