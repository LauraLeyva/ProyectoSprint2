from django.db import models
from django.db.models.deletion import CASCADE
from .Formula_Encabezado import FormulaEncabezado
from .Medicamentos import Medicamentos

class FormulaDetalle(models.Model):
    id_Formula_Detalle = models.AutoField(primary_key=True)    
    id_Formula_Encabezado=models.ForeignKey(FormulaEncabezado,related_name='Formula_Detalle',on_delete=CASCADE)
    id_Medicamento =models.ForeignKey(Medicamentos,related_name='Formula_Detalle', on_delete=models.CASCADE)
    Cantidad = models.IntegerField('Cantidad')
    