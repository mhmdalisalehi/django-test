from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'home/home.html')


def products(request):
    return render(request,'home/product.html')
