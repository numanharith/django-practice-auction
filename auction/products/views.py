from products.forms import ProductForm
from django.shortcuts import render
from products.forms import ProductForm

# Create your views here.
def views_index(request):
    form = ProductForm()
    return render(request, 'products/index.html', {"form": form})