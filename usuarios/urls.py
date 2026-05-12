from django.urls import path
from usuarios.views import iniciar_sesion, perfil_usuario, registrar_usuario, perfil_editar, editar_contrasenia_usuario
from django.contrib.auth.views import LogoutView


app_name='usuarios'

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion/', LogoutView.as_view(template_name='usuarios/sesion_cerrada.html'), name='sesion_cerrada'),
    path('registrar_usuario/', registrar_usuario, name='registrar_usuario'),
    path('perfil_usuario/', perfil_usuario, name='perfil_usuario'),
    path('perfil_usuario/editar_perfil/', perfil_editar, name='editar_perfil'),
    path('editar_contrasenia/', editar_contrasenia_usuario.as_view(), name='editar_contrasenia'),
]