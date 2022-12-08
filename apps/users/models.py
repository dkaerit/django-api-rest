from django.db import models
from django import forms


# @brief clase auxilial para la generacón de entradas en la base de datos
# @params Model, 

class UserModel(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)