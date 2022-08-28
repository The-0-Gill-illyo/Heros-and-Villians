from rest_framework import serializers
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter-ego', 'primary_ability', 'second_ability', 'catch_phrase', 'Super_type_id']