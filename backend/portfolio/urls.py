from django.urls import path
from rest_framework import routers
from .views import *


urlpatterns = [
    path('users/',UserViewSet.as_view({'get': 'list_users'}),name="users_all"),
    path('transactions/<username>',TransactionsViewSet.as_view({'get':'retrieve'}),name="user_trans")
]