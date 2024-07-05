from django.shortcuts import render
from .models import Product


def ProductList(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'store/product_list.html', context)