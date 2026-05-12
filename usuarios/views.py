from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from usuarios.forms import formulario_inicio_sesion, formulario_registro_usuario, formulario_editar_perfil, formulario_editar_contrasenia_usuario
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios.models import datos_usuario   

def iniciar_sesion(request):

    if request.method == 'POST':
        formulario = formulario_inicio_sesion(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            datos_usuario.objects.get_or_create(user=usuario)
            return redirect('home:home')
    else:
        formulario = formulario_inicio_sesion()

    return render(request, 'usuarios/iniciar_sesion.html',{'formulario': formulario})


def registrar_usuario(request):
    if request.method == 'POST':
        formulario = formulario_registro_usuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:iniciar_sesion')
    else:
        formulario = formulario_registro_usuario()

    return render(request, 'usuarios/registrar_usuario.html', {'formulario': formulario})

@login_required
def perfil_usuario(request):
    return render(request, 'usuarios/perfil_usuario.html')

@login_required
def perfil_editar(request):

    datos_usuario = request.user.datos_usuario

    if request.method == 'POST':
        formulario =formulario_editar_perfil(request.POST, instance=request.user)
        if formulario.is_valid():

            datos_usuario.biografia = formulario.cleaned_data.get('biografia')
            datos_usuario.save()

            formulario.save()
            return redirect('usuarios:perfil_usuario')
    else:
        formulario =formulario_editar_perfil(instance=request.user, initial={'biografia': datos_usuario.biografia})
    
    return render(request, 'usuarios/editar_perfil.html',{'formulario':formulario})

class editar_contrasenia_usuario(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/editar_contrasenia.html'
    success_url = reverse_lazy('usuarios:perfil_usuario')
    form_class= formulario_editar_contrasenia_usuario