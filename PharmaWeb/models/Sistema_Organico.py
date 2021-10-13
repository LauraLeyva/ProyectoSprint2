from django.db import models

class Sistema_Organico(models.Model):
    id_Sistema_Organico = models.CharField('id_SistemaOrganico ', max_length = 1,primary_key=True)
    Sistema_Organico = models.CharField('Sistema_Organico', max_length = 256)