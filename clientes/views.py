from django.shortcuts import render
from clientes.models import clientes

def listado(request):

    listado= clientes.objects.all()

    return render(request, 'clientes/listado.html',{'listado':listado})
