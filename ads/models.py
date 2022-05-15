from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)


class Ad(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    price = models.PositiveBigIntegerField()
    description = models.TextField(max_length=1000, null=True)
    address = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
