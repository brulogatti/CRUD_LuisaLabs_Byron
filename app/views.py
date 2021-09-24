from django.shortcuts import render
from app.forms import ProductsForm, CompaniesForm
from app.models import Products, Companies

# Create your views here.

def home(request):
    return render(request,'index.html')

def mnu_companies(request):
    data={}
    data['db'] = Companies.objects.all()
    return render(request,'mnu_companies.html', data)

def mnu_products(request):
    data={}
    data['db'] = Products.objects.all()
    return render(request,'mnu_products.html', data)

def form_companies(requests):
    data = {}
    data['form'] = CompaniesForm
    return render(requests, 'form_companies.html', data)

def form_products(requests):
    data = {}
    data['form'] = ProductsForm
    return render(requests,'form_products.html', data)

def create_product(request):
    form_products = ProductsForm(request.POST or None)
    if form_products.is_valid():
        form_products.save()
        return render(request, 'mnu_products.html')

def create_company(request):
    form_companies = CompaniesForm(request.POST or None)
    if form_companies.is_valid():
        form_companies.save()
        return render(request, 'mnu_companies.html')

