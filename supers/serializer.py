from rest_framework import serializers

from super_types.models import Super_type
from .models import Super

class SuperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'primary_ability', 'second_ability', 'catchphrase', 'Super_type_id']
        depth = 1

Super_type_id = serializers.IntegerField(write_only=True)