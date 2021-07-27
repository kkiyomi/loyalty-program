from django.urls import path
from .views import *

urlpatterns = [
    path("maker/", MakerListAPIView.as_view()),
    path("maker/<uid>", MakerRetrieveAPIView.as_view()),
    path("promo/<maker_uid>/", PromoCreateAPIView.as_view()),
]
