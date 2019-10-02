from rest_framework import serializers
from .models import *


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = [
            'symbol',
            'lastUpdated',
            'volume',
            '_open',
            '_high',
            '_low',
            '_close'
        ]
class StockUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockUser
        fields = [
            'userID', 
            'userName', 
            'bank'
        ]
class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = [
            'user',
            'stock',
            'shares',
            'amount_payed',
            'time'
        ]