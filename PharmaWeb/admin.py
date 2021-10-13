from django.contrib import admin
from .models.user import User
from .models.account import Account
from .models.Presentacion import Presentacion
from .models.Laboratorios import Laboratorios
from .models.Medicamentos import Medicamentos
from .models.FormaFarmaceutica import FormaFamaceutica
from .models.Subgrupo_Farmacologico import Subgrupo_Farmacologico
from .models.Subgrupo_Quimico import Subgrupo_Quimico
from .models.Grupo_Farmacologico import Grupo_Farmacologico
from .models.Sistema_Organico import Sistema_Organico
from .models.Genericos import Genericos
from .models.entidades import Entidades
from .models.consecutivos import Consecutivos
from .models.Pacientes import Pacientes
from .models.Profesionales import Profesionales
from .models.Formula_Encabezado import FormulaEncabezado
from .models.Formula_Detalle import FormulaDetalle
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Presentacion)
admin.site.register(Laboratorios)
admin.site.register(Medicamentos)
admin.site.register(FormaFamaceutica)
admin.site.register(Subgrupo_Farmacologico)
admin.site.register(Subgrupo_Quimico)
admin.site.register(Grupo_Farmacologico)
admin.site.register(Sistema_Organico)
admin.site.register(Genericos)
admin.site.register(Entidades)
admin.site.register(Consecutivos)
admin.site.register(Pacientes)
admin.site.register(Profesionales)
admin.site.register(FormulaEncabezado)
admin.site.register(FormulaDetalle)

# Register your models here.
