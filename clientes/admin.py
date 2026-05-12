from django.contrib import admin
from clientes.models import clientes



class clientes_admin_model(admin.ModelAdmin):
    list_filter = ('nombre', 'apellido', 'email', 'salario')
    list_display = ('nombre', 'apellido', 'email', 'salario')

admin.site.register(clientes, clientes_admin_model)