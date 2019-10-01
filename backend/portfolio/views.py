from django.shortcuts import render
from .models import *
# Create your views here.
from .serializers import *
from rest_framework import viewsets,response

class UserViewSet(viewsets.ViewSet):

    def list_users(self, request):
        queryset = StockUser.objects.all()
        serializer = StockUserSerializer(queryset, many=True)
        return response.Response(serializer.data)

    


class TransactionsViewSet(viewsets.ViewSet):
    def retrieve(self,request):
        #get the user first
        #Article.objects.filter(user=user)

        username = self.kwargs['username']
        
        return response.Response(username)