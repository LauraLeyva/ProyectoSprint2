from django.db import models

from PharmaWeb.models.Sistema_Organico import Sistema_Organico
from .FormaFarmaceutica import FormaFamaceutica
from .Subgrupo_Farmacologico import Subgrupo_Farmacologico
from .Subgrupo_Quimico import Subgrupo_Quimico
from .Grupo_Farmacologico import Grupo_Farmacologico
from .Sistema_Organico import Sistema_Organico



class Genericos(models.Model):
    id_Generico = models.CharField('id_Generico', max_length = 7,primary_key=True)
    Genericos = models.CharField('Genericos', max_length = 256)
    id_Sistema_Organico=models.ForeignKey(Sistema_Organico,related_name='Genericos', on_delete=models.CASCADE)
    id_Grupo_Farmacologico=models.ForeignKey(Grupo_Farmacologico,related_name='Genericos', on_delete=models.CASCADE)
    id_Subgrupo_Quimico=models.ForeignKey(Subgrupo_Quimico,related_name='Genericos', on_delete=models.CASCADE)
    id_SubgrupoFarmacologico=models.ForeignKey(Subgrupo_Farmacologico,related_name='Genericos', on_delete=models.CASCADE)
    id_FormaFamaceutica=models.ForeignKey(FormaFamaceutica,related_name='Genericos', on_delete=models.CASCADE)
   




    # user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)