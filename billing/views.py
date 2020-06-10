from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
# forms
from .forms import GenerateBillForm
# models from inventory
from madmin.models import Product
# test 
def AddCustomer(request):
  if request.method == 'POST':
    form = GenerateBillForm(request.POST)
    if form.is_valid():
      customer = form.save()
      messages.success(request, f'{customer.fname} inserted in databse, Bill will be generated shortly...')
      return redirect('Adding Customer')
  else:
    form = GenerateBillForm()
  context = {
    'form' : form
  }
  return render(request, 'billing/AddCustomer.html', context)
