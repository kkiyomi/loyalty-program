from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from users.models import *
from qrmaker.models import *
from qrmaker.api.pinstance.serializers import *


class PInstanceCreateTests(APITestCase):
    def setUp(self):
        self.user = Account.objects.create_user("username", "Pas$w0rd")
        self.client.force_authenticate(self.user)

        self.maker = self.user.maker
        self.promo = Promo.objects.create(maker=self.maker)

    def test_can_add(self):
        url = reverse("pinstance-create", args=[self.promo.suid])

        response = self.client.post(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PromoInstance.objects.count(), 1)
        self.assertTrue("Promo_Instance_" in PromoInstance.objects.get().title)

    def test_wrong_add(self):
        url = reverse("pinstance-create", args=["random"])

        response = self.client.post(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(PromoInstance.objects.count(), 0)


class PInstanceRUDTests(APITestCase):
    def setUp(self):
        self.user = Account.objects.create_user("username", "Pas$w0rd")
        self.client.force_authenticate(self.user)

        self.maker = self.user.maker
        self.promo = Promo.objects.create(maker=self.maker)
        self.pinstance = PromoInstance.objects.create(promo=self.promo)

    def test_can_get(self):
        url = reverse("pinstance-retrieve", args=[self.pinstance.uid])

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PromoInstance.objects.count(), 1)

    def test_can_get_list(self):
        url = reverse("pinstance-list", args=[self.promo.uid])

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
