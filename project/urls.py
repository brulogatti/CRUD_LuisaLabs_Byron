from django.contrib import admin
from django.urls import path
from app.views import home, mnu_companies, mnu_products,form_companies, form_products, create_company, \
    create_product, view_cmp, view_prod, edit_cmp, edit_prod, update_cmp, update_prod, delete_prod, delete_cmp

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
    path('edit_cmp/<int:pk>/', edit_cmp, name='edit_cmp'),
    path('edit_prod/<int:pk>/', edit_prod, name='edit_prod'),
    path('update_cmp/<int:pk>/', update_cmp, name='update_cmp'),
    path('update_prod/<int:pk>/',update_prod, name='update_prod'),
    path('delete_cmp/<int:pk>/',delete_cmp, name='delete_cmp'),
    path('delete_prod/<int:pk>/',delete_prod, name='delete_prod'),
]
