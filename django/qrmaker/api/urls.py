from django.urls import path
from .views import *

urlpatterns = [
    path("maker/", MakerListAPIView.as_view()),
    path("maker/<uid>/", MakerRetrieveAPIView.as_view()),
    path(
        "maker/<maker_uid>/promo/",
        PromoCreateAPIView.as_view(),
        name="promo-create",
    ),
    path(
        "promo/<maker_uid>/<promo_uid>/",
        PromoRUDAPIView.as_view(),
        name="promo-rud",
    ),
    path("code/<promo_suid>/", PInstanceCreateAPIView.as_view()),
]
