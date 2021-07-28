from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from qrmaker.models import *
from qrmaker.api.serializers import *


class PromoCreateTests(APITestCase):
    def setUp(self):
        self.maker = Maker.objects.create(username="User_1")

    def test_can_add_promo(self):
        data = {"title": "Promo_1", "description": "N/A", "size": 3}
        url = reverse("promo-create", args=[self.maker.uid])

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Promo.objects.count(), 1)
        self.assertEqual(Promo.objects.get().title, data["title"])

    def test_wrong_add_promo(self):
        data = {"title": "Promo_1", "description": "N/A", "size": 3}
        url = reverse("promo-create", args=["random"])

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Promo.objects.count(), 0)


class PromoRUDTests(APITestCase):
    def setUp(self):
        data = {"title": "Promo_1", "description": "N/A", "size": 3}
        self.maker = Maker.objects.create(username="User_1")
        self.promo = Promo.objects.create(**data, maker=self.maker)

    def test_wrong_promo(self):
        args = [
            "self.maker.uid",
            self.promo.uid,
        ]
        url = reverse("promo-rud", args=args)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        self.assertEqual(Promo.objects.count(), 1)

    def test_can_get_promo(self):
        url = reverse("promo-rud", args=[self.maker.uid, self.promo.uid])

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Promo.objects.count(), 1)
        self.assertEqual(response.data, PromoRUDSerializer(instance=self.promo).data)

    def test_can_edit_promo(self):
        data = {"title": "Promo_2", "description": "New", "size": 10}
        url = reverse("promo-rud", args=[self.maker.uid, self.promo.uid])

        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Promo.objects.count(), 1)

        self.assertEqual(Promo.objects.get().title, data["title"])
        self.assertEqual(Promo.objects.get().description, data["description"])
        self.assertEqual(Promo.objects.get().size, data["size"])

    def test_can_delete_promo(self):
        url = reverse("promo-rud", args=[self.maker.uid, self.promo.uid])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Promo.objects.count(), 0)
