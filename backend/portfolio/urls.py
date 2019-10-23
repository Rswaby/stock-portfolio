from django.urls import path
from rest_framework import routers
from .views import *


urlpatterns = [
    path(
        'users/', UserViewSet.as_view({'get': 'list_users'}), name="users_all"),
    path('users/<pk>',
         UserViewSet.as_view({'get': 'retrieve'}), name="users_by_pk"),
    path('users/create/',
         UserViewSet.as_view({'post': 'create'}), name="create_user"),
    path('transactions/',
         TransactionsViewSet.as_view({'post': 'create'}), name="create_trans"),
    path('transactions/<username>',
         TransactionsViewSet.as_view({'get': 'retrieve'}), name="user_trans"),
    path(
        'stock/', StockViewSet.as_view({'post': 'create'}), name="register_stock"),
    path('stock/<username>',
         StockViewSet.as_view({'get': 'user_stock'}, name='user_stocks')),
    path('live/<symbol>',
         LiveStocksViewSet.as_view({'get': 'retrieve'}), name='socket_connection'),
    path('live/<symbol>/daily', LiveStocksViewSet.as_view(
        {'get': 'retrieve_symbol_details'}), name='socket_connection')
]
