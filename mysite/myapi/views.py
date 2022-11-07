from django.shortcuts import render
from .serializers import ChampSerializer
from .models import Champions
from rest_framework import viewsets


class ChampionViewset(viewsets.ModelViewSet):
    queryset = Champions.objects.all().order_by('id')
    serializer_class = ChampSerializer

    
