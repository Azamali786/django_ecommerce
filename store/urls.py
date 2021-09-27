from django.urls import path,include
from . import views

app_name = "store_app"

urlpatterns = [
    path("", views.store, name="accounts_page"),
]