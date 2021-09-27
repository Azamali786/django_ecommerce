from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("store.urls", namespace="store_app")),
    path("account/", include("accounts.urls", namespace="accounts_app")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)