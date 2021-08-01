from django.db import models
from django.utils import timezone
from django.conf import settings

import uuid


class Maker(models.Model):

    username = models.CharField(max_length=200, default="N/A")

    title = models.CharField(max_length=200, default="N/A")
    description = models.TextField(default="N/A")
    date_added = models.DateTimeField(default=timezone.now)

    uid = models.CharField(default="", editable=False, max_length=100)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )

    def save(self, *args, **kwargs):

        if self.uid == "":
            self.uid = uuid.uuid4().hex
        if self.username == "N/A":
            self.username = "User_" + self.uid[:7]

        super(Maker, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class PromoState(models.TextChoices):
    Published = "Published"
    Pending = "Pending"
    Archived = "Archived"
    Completed = "Completed"
    Deleted = "Deleted"


class Promo(models.Model):
    title = models.CharField(max_length=200, default="N/A")
    description = models.TextField(default="N/A")
    date_added = models.DateTimeField(default=timezone.now)

    uid = models.CharField(default="", editable=False, max_length=100)
    suid = models.CharField(default="N/A", max_length=100)

    state = models.CharField(
        max_length=20, choices=PromoState.choices, default=PromoState.Pending
    )

    size = models.PositiveSmallIntegerField(default=1)

    maker = models.ForeignKey(
        Maker, on_delete=models.SET_NULL, related_name="promos", blank=True, null=True
    )

    def save(self, *args, **kwargs):

        if self.uid == "":
            self.uid = uuid.uuid4().hex

        if self.suid == "N/A":
            self.suid = self.uid[:10]

        if self.title == "N/A":
            self.title = "Promo_" + self.uid[:7]

        super(Promo, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class PromoInstance(models.Model):

    title = models.CharField(max_length=200, default="N/A")
    description = models.TextField(default="N/A")
    date_added = models.DateTimeField(default=timezone.now)

    uid = models.CharField(default="", editable=False, max_length=100)

    promo = models.ForeignKey(
        Promo,
        on_delete=models.SET_NULL,
        related_name="pinstances",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):

        if self.uid == "":
            self.uid = uuid.uuid4().hex
        if self.title == "N/A":
            self.title = "Promo_Instance_" + self.uid[:7]

        super(PromoInstance, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class Transaction(models.Model):

    title = models.CharField(max_length=200, default="N/A")
    description = models.TextField(default="N/A")
    date_added = models.DateTimeField(default=timezone.now)

    uid = models.CharField(default="", editable=False, max_length=100)

    pinstance = models.ForeignKey(
        PromoInstance,
        on_delete=models.SET_NULL,
        related_name="transactions",
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):

        if self.uid == "":
            self.uid = uuid.uuid4().hex
        if self.title == "N/A":
            self.title = "Transaction_" + self.uid[:7]

        super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"
