from django.db import models

# Create your models here.
class clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    salario = models.CharField(max_length=20)

    def __str__(self):
        return f"Cliente {self.pk}: {self.nombre} {self.apellido} - {self.email} - {self.salario}"