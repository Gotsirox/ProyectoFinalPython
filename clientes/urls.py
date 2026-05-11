from django.urls import path
from clientes.views import listado

app_name = 'clientes'

urlpatterns=[
    path('listado/', listado, name='listado'),
]