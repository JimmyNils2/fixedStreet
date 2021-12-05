from store.models import Product
from .cart import Cart
from django.shortcuts import redirect

# Create your views here.


def add_product(request,product_id):

    cart=Cart(request)

    product=Product.objects.get(id=product_id)

    cart.add(product=product)

    return(redirect('store'))


def delete_product(request,product_id):

    cart=Cart(request)

    product=Product.objects.get(id=product_id)

    cart.delete(product=product)

    return(redirect('store'))


def subtract_product(request,product_id):
    
    cart=Cart(request)

    product=Product.objects.get(id=product_id)

    cart.subtract(product=product)

    return(redirect('store'))


def empty_cart(request):

    cart=Cart(request)

    cart.empty()

    return(redirect('store')) 