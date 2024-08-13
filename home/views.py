from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages

from .models import *


def home(request):
    category = Category.objects.filter(is_subcategory=False)
    context = {'category': category}
    return render(request, 'home/home.html',context)


def products(request, slug=None, id=None):
    product = Product.objects.all()
    category = Category.objects.all()
    if slug and id:
        data = get_object_or_404(category, slug=slug, id=id)
        product = Product.objects.filter(category=data)

    context = {'product': product, 'category': category}
    return render(request,'home/product.html',context)


def product_details(request,slug,id):
    product = get_object_or_404(Product, slug=slug,id=id)

    return render(request,'home/details.html',{'product':product})


def navbar(request):
    category = Category.objects.all()
    return render(request,'navbar.html',{'category':category})