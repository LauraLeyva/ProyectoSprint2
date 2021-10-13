"""ciclo3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from PharmaWeb import views
from PharmaWeb.views import entidad_api_view
from PharmaWeb.views import entidad_detalle_api_view
from PharmaWeb.views import consecutivo_api_view
from PharmaWeb.views import consecutivo_detalle_api_view
from PharmaWeb.views import FormaFarmaceutica_api_view
from PharmaWeb.views import FormaFarmaceutica_detalle_api_view
from PharmaWeb.views import FormulaDetalle_api_view
from PharmaWeb.views import FormulaDetalle_detalle_api_view
from PharmaWeb.views import FormulaEncabezado_api_view
from PharmaWeb.views import FormulaEncabezado_detalle_api_view
from PharmaWeb.views import Genericos_api_view
from PharmaWeb.views import Genericos_detalle_api_view
from PharmaWeb.views import Grupo_Farmacologico_api_view
from PharmaWeb.views import Grupo_Farmacologico_detalle_api_view
from PharmaWeb.views import Laboratorios_api_view
from PharmaWeb.views import Laboratorios_detalle_api_view
from PharmaWeb.views import Medicamentos_api_view
from PharmaWeb.views import Medicamentos_detalle_api_view
from PharmaWeb.views import Pacientes_api_view
from PharmaWeb.views import Pacientes_detalle_api_view
from PharmaWeb.views import Presentacion_api_view
from PharmaWeb.views import Presentacion_detalle_api_view
from PharmaWeb.views import Profesionales_api_view
from PharmaWeb.views import Profesionales_detalle_api_view
from PharmaWeb.views import Sistema_Organico_api_view
from PharmaWeb.views import Sistema_Organico_detalle_api_view
from PharmaWeb.views import Subgrupo_Farmacologico_api_view
from PharmaWeb.views import Subgrupo_Farmacologico_detalle_api_view
from PharmaWeb.views import Subgrupo_Quimico_api_view
from PharmaWeb.views import Subgrupo_Quimico_detalle_api_view

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('Laboratorios/', Laboratorios_api_view,name='Laboratorios_detalle_api'),
    path('Laboratorios/<int:pk>/', Laboratorios_detalle_api_view,name='Laboratorios_detalle_api'),
    path('ConsecutivosCreateView/', consecutivo_api_view,name='consecutivo_api'),
    path('ConsecutivosCreateView/<int:pk>/', consecutivo_detalle_api_view,name='consecutivo_detalle_api'),
    path('EntidadesCreateView/', entidad_api_view,name='Entidad_api'),
    path('EntidadesCreateView/<int:pk>/', entidad_detalle_api_view,name='Entidad_detalle_api'),
    path('FormaFarmaceuticaCreateView/',  FormaFarmaceutica_api_view,name='FormaFarmaceutica_api'),
    path('FormaFarmaceuticaCreateView/<int:pk>/', FormaFarmaceutica_detalle_api_view,name='FormaFarmaceutica_detalle_api'),
    path('GrupoFarmacologicoCreateView/',Grupo_Farmacologico_api_view,name='GrupoFarmacologico_detalle_api'),
    path('GrupoFarmacologicoCreateView/<int:pk>/',Grupo_Farmacologico_detalle_api_view,name='GrupoFarmacologico_detalle_api'),
    path('PacientesCreateView/',Pacientes_api_view,name='Pacientes_detalle_api'),
    path('PacientesCreateView/<int:pk>/',Pacientes_detalle_api_view,name='Pacientes_detalle_api'),
    path('PresentacionCreateView/',Presentacion_api_view,name='Presentacion_detalle_api'),
    path('PresentacionCreateView/<int:pk>/',Presentacion_detalle_api_view,name='Presentacion_detalle_api'),
    path('ProfesionalesCreateView/',Profesionales_api_view,name='Profesionales_detalle_api'),
    path('ProfesionalesCreateView/<int:pk>/',Profesionales_detalle_api_view,name='Profesionales_detalle_api'),
    path('SistemaOrganicoCreateView/',Sistema_Organico_api_view,name='SistemaOrganico_detalle_api'),        
    path('SistemaOrganicoCreateView/<int:pk>/',Sistema_Organico_detalle_api_view,name='SistemaOrganico_detalle_api'),
    path('SubGrupo_FarmacologicoCreateView/',Subgrupo_Farmacologico_api_view,name='SistemaOrganico_detalle_api'),
    path('SubGrupo_FarmacologicoCreateView/<int:pk>/',Subgrupo_Farmacologico_detalle_api_view,name='SistemaOrganico_detalle_api'),
    path('SubGrupo_QuimicoCreateView/',Subgrupo_Quimico_api_view,name='SubGrupo_Quimico_detalle_api'),
    path('SubGrupo_QuimicoCreateView/<int:pk>/',Subgrupo_Quimico_detalle_api_view,name='SubGrupo_Quimico_detalle_api'),
    path('MedicamentoCreateView/',Medicamentos_api_view,name='Medicamento_detalle_api'),
    path('MedicamentoCreateView/<int:pk>/',Medicamentos_detalle_api_view,name='Medicamento_detalle_api'),
    path('genericosCreateView/',Genericos_api_view,name='Genericos_detalle_api'),
    path('genericosCreateView/<int:pk>/',Genericos_detalle_api_view,name='Genericos_detalle_api'),
    path('formulaencabezadoCreateView/',FormulaEncabezado_api_view,name='FormulaEncabezado_detalle_api'),
    path('formulaencabezadoCreateView/<int:pk>/',FormulaEncabezado_detalle_api_view,name='FormulaEncabezado_detalle_api'),
    path('formuladetalleCreateView/',FormulaDetalle_api_view,name='FormulaDetalle_detalle_api'),
    path('formuladetalleCreateView/<int:pk>/', FormulaDetalle_detalle_api_view,name='FormulaDetalle_detalle_api'),
    ]
