from django.shortcuts import render, redirect
from app.forms import ProductsForm, CompaniesForm
from app.models import Products, Companies

# Create your views here.

def home(request):
    return render(request,'index.html')

def mnu_companies(request):
    data={}
    search = request.GET.get('search')
    if search:
        data['db'] = Companies.objects.filter(cmpName__icontains=search)
    else:
        data['db'] = Companies.objects.all()
    return render(request,'mnu_companies.html', data)

def mnu_products(request):
    data={}
    search = request.GET.get('search')
    if search:
        if(Products.objects.filter(prodCompany__icontains=search)):
            data['db']=Products.objects.filter(prodCompany__icontains=search)
        else:
            data['db'] = Products.objects.filter(prodName__icontains=search)
    else:
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
        return redirect('mnu_products')

def create_company(request):
    form_companies = CompaniesForm(request.POST or None)
    if form_companies.is_valid():
        form_companies.save()
        return redirect( 'mnu_companies')

def view_cmp(request, pk):
    data={}
    data['db']=Companies.objects.get(pk=pk)
    return render(request,'view_cmp.html', data)

def view_prod(request,pk):
    data={}
    data['db']=Products.objects.get(pk=pk)
    return render (request,'view_prod.html', data)

def edit_cmp(request, pk):
    data={}
    data['db']=Companies.objects.get(pk=pk)
    data['form']=CompaniesForm(instance=data['db'])
    return render(request, 'form_companies.html', data)

def edit_prod(request, pk):
    data={}
    data['db']=Products.objects.get(pk=pk)
    data['form']=ProductsForm(instance=data['db'])
    return render(request, 'form_products.html', data)

def update_cmp(request, pk):
    data ={}
    data['db']=Companies.objects.get(pk=pk)
    form=CompaniesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('mnu_companies')

def update_prod(request, pk):
    data ={}
    data['db']=Products.objects.get(pk=pk)
    form=ProductsForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('mnu_products')

def delete_cmp(request,pk):
    db = Companies.objects.get(pk=pk)
    db.delete()
    return redirect('mnu_companies')

def delete_prod(request, pk):
    db=Products.objects.get(pk=pk)
    db.delete()
    return redirect('mnu_products')

# def search(request):
#     data = {}
#     search = request.GET.get('search')
#     if search:
#         data['db'] = Companies.objects.filter(cmpName__icontains=search)
#     return render(request, 'search.html', data)
#


