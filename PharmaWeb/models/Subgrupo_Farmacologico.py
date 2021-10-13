from django.db import models


class Subgrupo_Farmacologico(models.Model):
    id_SubgrupoFarmacologico = models.CharField('id_SubgrupoFarmacologico', max_length = 5,primary_key=True)
    Subgrupo_Farmacologico = models.CharField('Subgrupo_Farmacologico', max_length = 256)