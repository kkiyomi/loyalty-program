from rest_framework import serializers
from users.models import *


class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["email", "date_joined", "last_login"]
