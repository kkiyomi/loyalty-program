from django.urls import path

from .promo.views import *
from .maker.views import *
from .pinstance.views import *
from .transaction.views import *


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
    path(
        "code/<promo_suid>/",
        PInstanceCreateAPIView.as_view(),
        name="pinstance-create",
    ),
    path(
        "instance/<pinstance_uid>/",
        PInstanceRetrieveAPIView.as_view(),
        name="pinstance-r",
    ),
    path(
        "transact/<pinstance_uid>/",
        TransactionCreateAPIView.as_view(),
        name="transaction-create",
    ),
    path(
        "transaction/<transaction_uid>/",
        TransactionRetrieveAPIView.as_view(),
        name="transaction-r",
    ),
]
