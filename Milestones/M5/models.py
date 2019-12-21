from django.db import models
import uuid
from datetime import date
from django.contrib.auth.models import User


# Create your models here.
class ReceiptModel(models.Model):
	#user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    print("got image")


class ItemModel(models.Model):
    item_name = models.CharField(max_length=100)
    # pur_date = models.DateField()
    exp_date = models.DateField()
    cal = models.PositiveIntegerField(max_length=5)
    # uid = models.UUIDField(default=uuid.uuid4, editable=False)
    


class SearchModel(models.Model):
    search = models.CharField(max_length=100)
    print("Searched")
