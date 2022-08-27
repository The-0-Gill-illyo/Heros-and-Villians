from unicodedata import name
from django.db import models
from super_types.models import Super_type

# Create your models here.


class Super(models.Model):
    name = models.CharField(max_length=255)
    alter_ego = models.CharField(max_length=255)
    primary_ability = models.CharField(max_length=255)
    second_ability = models.CharField(max_length=255)
    catch_pharse = models.CharField(max_length=255)
    Super_type = models.ForeignKey(Super_type, on_delete=models.CASCADE)
