
from django.contrib import admin
from django.urls import path
from .views import home, infoDiaEstado, infoDiaBrasil

urlpatterns = [
    path('', home),
    path('info_dia_estado', infoDiaEstado, name="dataInfoDiaEstado"),
    path('info_dia_brasil', infoDiaBrasil, name="dataInfoDiaBrasil"),

]
