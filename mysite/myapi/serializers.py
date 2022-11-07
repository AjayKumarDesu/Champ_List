from rest_framework import serializers
from .models import Champions


class ChampSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champions
        fields = ('id', 'name', 'div')