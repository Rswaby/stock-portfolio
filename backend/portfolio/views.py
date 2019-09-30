from django.shortcuts import render
from .models import *
# Create your views here.
from .serializers import *
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class = StockUserSerializer
    queryset = StockUser.objects.all()