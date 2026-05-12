from django.db import models
from django.contrib.auth.models import User



class datos_usuario(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    biografia= models.TextField()
    avatar= models.ImageField(upload_to='avatares', null=True, blank=True)