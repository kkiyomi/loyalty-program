from django.urls import path, include
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView
from .views import *

urlpatterns = [
    path("", AccountRetrieveAPIView.as_view(), name="user_account"),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "auth/account-confirm-email/<key>/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    path(
        "auth/account-confirm-reset/<uidb64>/<token>",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
]
