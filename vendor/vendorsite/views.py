from django.shortcuts import render
from rest_framework import generics

from .models import Test
from .serializers import TestSerializer

class TestListCreate(generics.ListCreateAPIView):
    queryset= Test.objects.all()
    serializer_class =  TestSerializer

# Create your views here.
