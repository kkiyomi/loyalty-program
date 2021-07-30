from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from qrmaker.models import *
from qrmaker.api.pinstance.serializers import *


class PInstanceCreateTests(APITestCase):
    def setUp(self):
        self.maker = Maker.objects.create(username="User_1")
        self.promo = Promo.objects.create(maker=self.maker)

    def test_can_add_pinstance(self):
        data = {}
        url = reverse("pinstance-create", args=[self.promo.suid])

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PromoInstance.objects.count(), 1)
        self.assertTrue("Promo_Instance_" in PromoInstance.objects.get().title)

    # def test_wrong_add_promo(self):
    #     data = {"title": "P_Instance_1", "description": "N/A", "size": 3}
    #     url = reverse("promo-create", args=["random"])

    #     response = self.client.post(url, data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    #     self.assertEqual(Promo.objects.count(), 0)
