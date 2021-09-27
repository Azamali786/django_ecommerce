
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("store.urls", namespace="store_app")),
    path("account/", include("accounts.urls", namespace="accounts_app")),
]
