from django.db import models
from .Laboratorios import Laboratorios


class Medicamentos(models.Model):
    id_Medicamento = models.AutoField(primary_key=True)
    Medicamento = models.CharField('Medicamento', max_length = 256)
    Existencia= models.IntegerField('Existencia')
    id_Laboratorio=models.ForeignKey(Laboratorios,related_name='Medicamentos', on_delete=models.CASCADE)
   
    