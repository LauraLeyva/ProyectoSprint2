from django.db import models


class Grupo_Farmacologico(models.Model):
    id_Grupo_Farmacologico = models.CharField('id_GrupoFarmacologico', max_length = 3,primary_key=True)
    Grupo_Farmacologico = models.CharField('GrupoFarmacologico', max_length = 256)