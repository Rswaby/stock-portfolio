from .models import *
from django.shortcuts import get_object_or_404
from .serializers import *
from rest_framework import viewsets, response, status
from alpha_vantage.timeseries import TimeSeries
from django.conf import settings


class UserViewSet(viewsets.ViewSet):

    def list_users(self, request):
        queryset = StockUser.objects.all()
        serializer = StockUserSerializer(queryset, many=True)
        return response.Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def create(self, request):
        # assume that we cannot have dupplicate users
        serializer = StockUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        query_set = StockUser.objects.all()
        user = get_object_or_404(query_set, userID=pk)
        serializer = StockUserSerializer(user, many=False)
        print(serializer)

        return response.Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class TransactionsViewSet(viewsets.ViewSet):

    def retrieve(self, request, username=None):
        queryset = StockUser.objects.all()
        user = get_object_or_404(queryset, userID=username)
        queryset2 = Transactions.objects.filter(user=user)
        serializer = TransactionsSerializer(queryset2, many=True)

        return response.Response(serializer.data, status.HTTP_200_OK)

    def create(self, request):
        serializer = TransactionsSerializer(data=request.data)
        # update-user-rohan
        userEntry = StockUser.objects.get(userID=request.data.get('user'))
        remainder = userEntry.bank - request.data.get('amount_payed')
        userEntry.bank = remainder

        if serializer.is_valid():
            returnval = dict()

            userEntry.save()
            serializer.save()
            returnval['moneyLeft'] = remainder
            returnval['transaction'] = serializer.data
            return response.Response(returnval, status=status.HTTP_201_CREATED)
        else:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        pass


class StockViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        query_set = Stock.objects.all()
        serializer = StockSerializer(query_set, many=True)
        return response.Response(serializer.data, status.HTTP_200_OK)

    def user_stock(self, request, username=None):
        query_set = Transactions.objects.all()
        # find a way to get all stocks for x user
        pass

    def update(self, request):
        query_set = Stock.objects.all()
        #ts = TimeSeries(key='1CUKM2S9MK37DA21', output_format='json')
        #data, meta_data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')
        # last_refreshed = meta_data['3. Last Refreshed']
        # data[last_refreshes] to get most recent data value
        # print(meta_data)
        # go through all the stocks and update there values

    def retrieve(self, request, symbol=None):
        query_set = Stock.objects.all()
        subset = get_object_or_404(symbol=symbol)
        serializer = StockSerializer(subset)
        return response.Response(serializer.data, status.HTTP_200_OK)


class LiveStocksViewSet(viewsets.ViewSet):

    def live_update(self, request):
        pass

    def retrieve(self, request, symbol=None):
        # search_symbol
        # reimplement  https://www.alphavantage.co/documentation/#symbolsearch
        ts = TimeSeries(key=settings.API_KEY, output_format='json')
        data, meta_data = ts.get_symbol_search(symbol)
        print(meta_data)
        return response.Response(data)

    def retrieve_symbol_details(self, request, symbol=None):
        ts = TimeSeries(key=settings.API_KEY, output_format='json')
        data, meta_data = ts.get_intraday(symbol=symbol)
        last_refreshed = meta_data['3. Last Refreshed']
        data = data[last_refreshed]
        result = {}
        result['data'] = data
        result['meta_data'] = meta_data

        return response.Response(result)

    # def update_stock_information(self,request):
