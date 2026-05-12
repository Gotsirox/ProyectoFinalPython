from django import forms
from clientes.models import cliente


class formulario_cliente(forms.ModelForm):
    
    class Meta:
        model= cliente
        fields= '__all__'

class formulario_busqueda(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)
    apellido = forms.CharField(max_length=100, required=False)
    email = forms.CharField(max_length=100, required=False)
    salario = forms.CharField(max_length=100, required=False)