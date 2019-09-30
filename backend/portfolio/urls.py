from django.urls import path
from rest_framework import routers
from .views import UserViewSet


urlpatterns = [
    path('users/',UserViewSet.as_view(),name="users_all")
]