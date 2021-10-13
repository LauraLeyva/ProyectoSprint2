from django.db import models


class Entidades(models.Model):
    id_Entidad = models.AutoField(primary_key=True)
    Razon_social = models.CharField('Entidades', max_length = 256)