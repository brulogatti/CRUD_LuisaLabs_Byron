"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from app.views import home, mnu_companies, mnu_products,form_companies, form_products, create_company, create_product, view_cmp, view_prod

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('mnu_companies', mnu_companies, name ='mnu_companies'),
    path('mnu_products', mnu_products, name='mnu_products'),
    path('form_companies/', form_companies, name='form_companies'),
    path('form_products/', form_products, name='form_project'),
    path('create_company/', create_company, name='create_company'),
    path('create_product/', create_product, name='create_product'),
    path('view_cmp/<int:pk>/', view_cmp, name = 'view_cmp'),
    path('view_prod/<int:pk>/', view_prod, name = 'view_prod'),
]
