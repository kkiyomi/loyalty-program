from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/user/", include("users.api.urls")),
    path("api/qr/", include("qrmaker.api.urls")),
]
