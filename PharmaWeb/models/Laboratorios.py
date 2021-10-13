from django.db import models


class Laboratorios(models.Model):
    id_Laboratorio = models.AutoField(primary_key=True)
    Laboratorio = models.CharField('Laboratorio', max_length = 256)
    