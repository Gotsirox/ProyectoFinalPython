from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from clientes.models import cliente
from clientes.forms import formulario_cliente, formulario_busqueda
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def listado(request):


    formulario=formulario_busqueda(request.GET)
    if formulario.is_valid():
        listado= cliente.objects.filter(nombre__icontains=formulario.cleaned_data.get('nombre'), apellido__icontains=formulario.cleaned_data.get('apellido'), email__icontains=formulario.cleaned_data.get('email'), salario__icontains=formulario.cleaned_data.get('salario'))
    else:
        listado= cliente.objects.all()

    return render(request, 'clientes/listado.html',{'listado':listado, 'formulario': formulario})

@login_required
def crear_cliente(request):

    if request.method=='POST':
        formulario= formulario_cliente(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect('clientes:listado')
    else:
        formulario= formulario_cliente()
        return render(request, 'clientes/crear_cliente.html', {'formulario': formulario})

def detalle_cliente(request, id):
    Clientes = cliente.objects.get(id=id)
    return render(request, 'clientes/detalle_cliente.html', {'cliente': Clientes})

class borrar_cliente(LoginRequiredMixin, DeleteView):
    model = cliente
    template_name = 'clientes/borrar_cliente.html'
    success_url = reverse_lazy('clientes:listado')

class editar_cliente(LoginRequiredMixin, UpdateView):
    model = cliente
    template_name = 'clientes/editar_cliente.html'
    success_url = reverse_lazy('clientes:listado')
    form_class = formulario_cliente

def about(request):
    return render(request, 'clientes/about.html')