"""stockapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from django.views.generic import TemplateView


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    # re_path(r'^$', schema_view),
    path('admin/', admin.site.urls),
    re_path('api/', include('backend.portfolio.urls')),
    path('openapi/', get_schema_view(
        title="Stock Porfolio",
        description="API developers hpoing to use our service"
    ), name='openapi-schema'),

    re_path(r'^$', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
]
