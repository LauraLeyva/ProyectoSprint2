from django.db import models

from PharmaWeb.models.Pacientes import Pacientes
from .consecutivos import Consecutivos
from .Profesionales import Profesionales
from .user import User

class FormulaEncabezado(models.Model):
    id_Formula_Encabezado = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='Formula_Encabezado', on_delete=models.CASCADE)
    Fecha_Formula = models.DateField('Fecha_Formula', max_length = 10)
    Registro_Medico=models.ForeignKey(Profesionales, related_name='Formula_Encabezado', on_delete=models.CASCADE)
    Cod_Paciente=models.ForeignKey(Pacientes, related_name='Formula_Encabezado', on_delete=models.CASCADE)
    id_Consecutivo=models.ForeignKey(Consecutivos, related_name='Formula_Encabezado', on_delete=models.CASCADE)