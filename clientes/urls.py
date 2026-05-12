from django.urls import path
from clientes.views import detalle_cliente, listado, crear_cliente, borrar_cliente, editar_cliente, about

app_name = 'clientes'

urlpatterns=[
    path('about/', about, name='about'),
    path('listado/', listado, name='listado'),
    path('crear/', crear_cliente, name='crear_cliente'),
    path('<id>/', detalle_cliente, name='detalle_cliente'),
    path('<pk>/editar_cliente/', editar_cliente.as_view(), name='editar_cliente'),
    path('<pk>/borrar_cliente/', borrar_cliente.as_view(), name='borrar_cliente'),
    ]