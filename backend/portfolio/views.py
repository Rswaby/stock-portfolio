from django.shortcuts import render
from .models import *
# Create your views here.
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets,response

class UserViewSet(viewsets.ViewSet):

    def list_users(self, request):
        queryset = StockUser.objects.all()
        serializer = StockUserSerializer(queryset, many=True)
        return response.Response(serializer.data)



class TransactionsViewSet(viewsets.ViewSet):
    def retrieve(self,request,pk=None):
        queryset = StockUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        
        return response.Response(user)