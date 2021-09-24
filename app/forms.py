from django.forms import ModelForm
from app.models import Companies, Products


class CompaniesForm(ModelForm):
    class Meta:
        model = Companies
        fields = ['cmpId', 'cmpCnpj', 'cmpName', 'cmpPassword', 'cmpAddress', 'cmpEmail', 'cmpPhone']

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields = ['prodId', 'prodName', 'prodCompany', 'prodDescription', 'prodPrice']
