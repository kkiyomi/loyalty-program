from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path("register/", RegistrationCreateAPIView.as_view(), name="registration"),
    path("login/", obtain_auth_token, name="login"),
    path("user/", AccountRetrieveAPIView.as_view(), name="user_account"),
]
