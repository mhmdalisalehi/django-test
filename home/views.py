from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


def home(request):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'home/home.html',context)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,'home/product.html',context)
