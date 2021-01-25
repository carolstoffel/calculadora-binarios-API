from django_filters.rest_framework import DjangoFilterBackend
from django.conf import settings
from django.core import serializers
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from binarios.models import CalculaBinarios
from .serializers import BinariosSerializer



class BinariosViewSet(viewsets.ModelViewSet):
    #queryset = CalculaBinarios.objects.all()
    serializer_class = BinariosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'operacao']

    def get_queryset(self):
        queryset = CalculaBinarios.objects.all()
        return queryset
