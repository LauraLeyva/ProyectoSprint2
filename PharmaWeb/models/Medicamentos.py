from django.db import models
from .Laboratorios import Laboratorios
from .Presentacion import Presentacion
from .Genericos import Genericos
class Medicamentos(models.Model):
    id_Medicamento = models.CharField('id_Medicamento', max_length = 100,primary_key=True)
    Medicamento = models.CharField('Medicamento', max_length = 256)
    Existencia= models.IntegerField('Existencia')
    id_Laboratorio=models.ForeignKey(Laboratorios,related_name='Medicamentos', on_delete=models.CASCADE)
    id_Presentacion=models.ForeignKey(Presentacion,related_name='Medicamentos', on_delete=models.CASCADE)
    id_Generico=models.ForeignKey(Genericos,related_name='Medicamentos', on_delete=models.CASCADE)