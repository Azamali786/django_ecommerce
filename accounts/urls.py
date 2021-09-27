from django.urls import path,include
from . import views

app_name = "accounts_app"

urlpatterns = [
    path("", views.accounts, name="accounts_page"),
]