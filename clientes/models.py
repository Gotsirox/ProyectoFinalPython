from django.db import models

# Create your models here.
class clientes(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    email = models.CharField()
    salario = models.CharField()

    def __str__(self):
        return f"Cliente {self.pk}: {self.nombre} {self.apellido} - {self.email} - {self.salario}"