from django.db import models


class Presentacion(models.Model):
    id_Presentacion = models.AutoField(primary_key=True)
    Presentacion = models.CharField('Presentacion', max_length = 256)