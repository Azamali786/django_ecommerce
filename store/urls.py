from django.urls import path,include
from . import views

app_name = "store_app"

urlpatterns = [
    path("", views.store, name="store_page"),

    path("cart/", views.cart, name="cart_page"),

    path("checkout/", views.checkout, name="checkout_page"),

    path("update_item/", views.update_item, name="update_item_page"),

    path("process_order/", views.process_order, name="process_order_page"),
]