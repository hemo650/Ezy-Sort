from django.db import models


# Create your models here.
class ReceiptModel(models.Model):
    image = models.ImageField()
    print("got image")


class SearchModel(models.Model):
    search = models.CharField(max_length=100)
    print("Searched")
