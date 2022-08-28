from rest_framework import serializers
from .models import Super_type

class SuperTypeClass(serializers.ModelSerializer):
    class Meta:
        model = Super_type
        fields = ['id', 'type']