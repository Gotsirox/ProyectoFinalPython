from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    email = models.CharField()
    salario = models.CharField()
    imagen = models.ImageField(upload_to='imagenes_clientes',null=True, blank=True)

    def __str__(self):
        return f"Cliente {self.pk}: {self.nombre} {self.apellido} - {self.email} - {self.salario}"