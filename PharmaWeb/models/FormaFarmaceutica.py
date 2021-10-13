from django.db import models


class FormaFamaceutica(models.Model):
    id_FormaFamaceutica = models.CharField('Id_FormaFamaceutica', max_length = 10,primary_key=True)
    FormaFamaceutica = models.CharField('FormaFamaceutica', max_length = 256)