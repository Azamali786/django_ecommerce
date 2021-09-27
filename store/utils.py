import json

from django.db.models.fields import PositiveIntegerRelDbTypeMixin
from .models import *
from django.core import serializers


def cookieCart(request):
    try:
        cart = json.loads(
            request.COOKIES["cart"]
        )  # remember dict object is not callable so use []
    except:
        cart = {}
    # print("value of cart is :", cart)

    items = []
    order = {"get_cart_items": 0, "get_cart_total": 0, "shipping": False}
    cartItems = order["get_cart_items"]

    for item in cart:

        try:
            cartItems += cart[item]["quantity"]
            product = Product.objects.get(id=item)
            total = product.price * cart[item]["quantity"]
            order["get_cart_total"] += total
            order["get_cart_items"] += cart[item]["quantity"]
            item = {
                "product": {
                    "id": product.id,
                    "name": product.name,
                    "price": product.price,
                    "imageURL": product.imageURL,
                },
                "quantity": cart[item]["quantity"],
                "get_total": total,
            }
            items.append(item)
            if product.digital == False:
                order["shipping"] = True
        except:
            pass
    return {"items": items, "orders": order, "cartItems": cartItems}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = serializers.serialize("json",queryset=order.orderitem_set.all())
        cartItems = order.get_cart_items

    else:
        cookieData = cookieCart(request)
        items = cookieData["items"]
        order = cookieData["orders"]
        cartItems = cookieData["cartItems"]

    return {
        "items": items,
        "orders": order,
        "cartItems": cartItems,
    }


def guestOrder(request, data):
    print("user is not logedin")
    name = data["userInfo"]["name"]
    email = data["userInfo"]["email"]
    print("customer info is :", name, email)

    cookieData = cookieCart(request)
    items = cookieData["items"]
    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    print("customer is ", customer.name)

    customer.name = name
    customer.save()
    order = Order.objects.create(customer=customer, complete=False)

    for item in items:
        product = Product.objects.get(id=item["product"]["id"])

        orderItem = OrderItem.objects.create(
            product=product, order=order, quantity=item["quantity"]
        )
    return customer, order
