from rest_framework import serializers
from models import Registry

""" Registry Serializer declaration """
class RegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Registry
        fields = ['id','service','version']