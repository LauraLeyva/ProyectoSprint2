from django.db import models


class Profesionales(models.Model):
    Registro_Medico = models.CharField('Registro_Medico',max_length = 30,primary_key=True)
    Tipodoc = models.CharField('TipoDoc', max_length = 3)
    IdDocumento = models.CharField('IDDocumento', max_length = 30)
    Pname = models.CharField('PName', max_length = 30)
    sname = models.CharField('SName', max_length = 30)
    Papellido = models.CharField('PApellido', max_length = 30)
    Sapellido = models.CharField('SApellido', max_length = 30)
    
  