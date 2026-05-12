from django.contrib import admin
from clientes.models import cliente



class clientes_admin_model(admin.ModelAdmin):
    list_filter = ('nombre', 'apellido', 'email', 'salario')
    list_display = ('nombre', 'apellido', 'email', 'salario')

admin.site.register(cliente, clientes_admin_model)