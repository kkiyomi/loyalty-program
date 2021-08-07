from django.urls import path

from .promo.views import *
from .maker.views import *
from .pinstance.views import *
from .transaction.views import *


urlpatterns = [
    path("maker/", MakerRetrieveAPIView.as_view()),
    path(
        "promo/",
        PromoCreateAPIView.as_view(),
        name="promo-create",
    ),
    path(
        "promo/<uid>/",
        PromoUpdateDestroyAPIView.as_view(),
        name="promo-update-destroy",
    ),
    path(
        "code/<promo_suid>/",
        PInstanceCreateAPIView.as_view(),
        name="pinstance-create",
    ),
    path(
        "instance/<uid>/",
        PInstanceRetrieveAPIView.as_view(),
        name="pinstance-retrieve",
    ),
    path(
        "add/<pinstance_uid>/",
        TransactionCreateAPIView.as_view(),
        name="transaction-create",
    ),
    path(
        "transaction/<transaction_uid>/",
        TransactionRetrieveAPIView.as_view(),
        name="transaction-r",
    ),
]
