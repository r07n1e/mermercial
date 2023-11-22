from django.db import models
from .basemodel import BaseModel
from .category import Category


class Product(BaseModel):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0)
    on_discount = models.BooleanField(default=False)
    discount_price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
