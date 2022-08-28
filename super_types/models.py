from django.db import models
from supers.models import Super

# Create your models here.

class Super_type(models.Model):
    type = models.CharField(max_length=255)
    