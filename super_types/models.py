from django.db import models
# from super_types.models import Super_type

# Create your models here.

class Super_type(models.Model):
    type = models.CharField(max_length=255)
    