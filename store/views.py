from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import *
from .utils import cartData

# Create your views here.


def store(request):
    data = cartData(request)
    # print(data)

    items = data["items"]
    order = data["orders"]
    cartItems = data["cartItems"]

    products = Product.objects.all()
    context = {
        "products": products,
        "items": items,
        "orders": order,
        "cartItems": cartItems,
    }
    return render(request, "store/store.html", context)


def cart(request):
    context = {}
    return render(request, "store/store.html", context)


def checkout(request):
    context = {}
    return render(request, "store/store.html", context)


def update_item(request):
    context = {}
    return render(request, "store/store.html", context)


def process_order(request):
    context = {}
    return render(request, "store/store.html", context)
