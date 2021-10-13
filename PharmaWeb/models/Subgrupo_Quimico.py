from django.db import models


class Subgrupo_Quimico(models.Model):
    id_Subgrupo_Quimico = models.CharField('id_SubgrupoQuimico', max_length = 5,primary_key=True)
    Subgrupo_Quimico = models.CharField('Subgrupo_Quimico', max_length = 256)