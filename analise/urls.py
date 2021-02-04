
from django.contrib import admin
from django.urls import path
from .views import home, infoDiaEstado

urlpatterns = [
    path('', home),
    path('info_dia_estado', infoDiaEstado, name="dataInfoDiaEstado"),

]
