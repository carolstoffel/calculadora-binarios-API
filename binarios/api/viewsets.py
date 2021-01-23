from django.conf import settings
from django.core import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from django.http import Http404
from django.shortcuts import render
from rest_framework import viewsets
from binarios.models import CalculaBinarios
from .serializers import BinariosSerializer
from django.http import JsonResponse
from rest_framework.decorators import action


class BinariosViewSet(viewsets.ModelViewSet):
    #queryset = CalculaBinarios.objects.all()
    serializer_class = BinariosSerializer

    def get_queryset(self):
        queryset = CalculaBinarios.objects.all()
        return queryset
