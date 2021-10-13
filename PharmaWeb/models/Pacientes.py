from django.db import models

from PharmaWeb.models.entidades import Entidades

class Pacientes(models.Model):
    Cod_Paciente = models.CharField('Cod_Paciente',max_length = 50,primary_key=True)
    Tipodoc = models.CharField('TipoDoc', max_length = 3)
    IdDocumento = models.CharField('IDDocumento', max_length = 30)
    Pname = models.CharField('PName', max_length = 30)
    sname = models.CharField('SName', max_length = 30)
    Papellido = models.CharField('PApellido', max_length = 30)
    Sapellido = models.CharField('SApellido', max_length = 30)
    id_Entidad=models.ForeignKey(Entidades,related_name='Pacientes', on_delete=models.CASCADE)
  