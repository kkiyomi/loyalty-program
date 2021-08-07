from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from users.models import *
from qrmaker.models import *
from qrmaker.api.promo.serializers import *


class PromoCreateTests(APITestCase):
    def setUp(self):
        self.user = Account.objects.create_user("username", "Pas$w0rd")
        self.client.force_authenticate(self.user)

    def test_can_add_promo(self):
        data = {"title": "Promo_1", "description": "N/A", "size": 3}
        url = reverse("promo-create")

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Promo.objects.count(), 1)
        self.assertEqual(Promo.objects.get().title, data["title"])


class PromoRUDTests(APITestCase):
    def setUp(self):
        self.user = Account.objects.create_user("username", "Pas$w0rd")
        self.client.force_authenticate(self.user)

        data = {"title": "Promo_1", "description": "N/A", "size": 3}
        self.maker = self.user.maker
        self.promo = Promo.objects.create(**data, maker=self.maker)

    def test_wrong_promo(self):
        data = {"title": "Promo_2", "description": "New", "size": 10}
        args = ["random"]
        url = reverse("promo-update-destroy", args=args)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        self.assertEqual(Promo.objects.count(), 1)

    def test_can_edit_promo(self):
        data = {"title": "Promo_2", "description": "New", "size": 10}
        url = reverse("promo-update-destroy", args=[self.promo.uid])

        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Promo.objects.count(), 1)

        self.assertEqual(Promo.objects.get().title, data["title"])
        self.assertEqual(Promo.objects.get().description, data["description"])
        self.assertEqual(Promo.objects.get().size, data["size"])

    def test_can_delete_promo(self):
        url = reverse("promo-update-destroy", args=[self.promo.uid])

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Promo.objects.get().state, "Deleted")
        self.assertEqual(Promo.objects.count(), 1)
