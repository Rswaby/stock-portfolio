from django.shortcuts import render
from .models import *
# Create your views here.
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets,response, status

class UserViewSet(viewsets.ViewSet):

    def list_users(self, request):
        queryset = StockUser.objects.all()
        serializer = StockUserSerializer(queryset, many=True)
        return response.Response(serializer.data,status=status.HTTP_202_ACCEPTED) 


    def create(self, request):
        #assume that we cannot have dupplicate users
        serializer = StockUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

    



class TransactionsViewSet(viewsets.ViewSet):

    def retrieve(self,request,username=None):
        queryset = StockUser.objects.all()
        user = get_object_or_404(queryset, userID=username)
        queryset2 = Transactions.objects.filter(user=user)
        serializer = TransactionsSerializer(queryset2, many=True)
        
        
        return response.Response(serializer.data,status.HTTP_200_OK)
    
    def create(self, request):
        serializer = TransactionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    

    def destroy(self, request, pk=None):
        pass

class StockViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        query_set = Stock.objects.all()
        serializer = StockSerializer(query_set,many=True)
        return response.Response(serializer.data,status.HTTP_200_OK)
    
    def retrieve(self, request, symbol=None):
        query_set = Stock.objects.all()
        subset = get_object_or_404(symbol=symbol)
        serializer = StockSerializer(subset)
        return response.Response(serializer.data,status.HTTP_200_OK)
        pass