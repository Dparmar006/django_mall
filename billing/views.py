from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# models from inventory
from madmin.models import Product
# test 
def test(request):
  products = Product.objects.all()
  context = {
    'products' : products
  }
  return render(request, 'billing/test.html', context)
