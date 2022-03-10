from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nome = models.CharField(max_length=125)
    email = models.CharField(max_length=125, unique=True)
    edv = models.IntegerField()
    senha = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []