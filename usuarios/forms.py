from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User


class formulario_inicio_sesion(AuthenticationForm):
    username= forms.CharField(label='Usuario', max_length=100)
    password= forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class formulario_registro_usuario(UserCreationForm):
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts ={
            'username': '',
            'email': '',
            }
        labels = {
            'username': 'Usuario',
            'email': 'Correo electrónico',
        }

class formulario_editar_perfil(UserChangeForm):
    password= None
    biografia= forms.CharField(widget=forms.Textarea)

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email',]
        labels = {
            'email': 'Correo electrónico',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
        }

class formulario_editar_contrasenia_usuario(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña Actual', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Confirmar Nueva Contraseña', widget=forms.PasswordInput)