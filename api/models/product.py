from django.db import models
from .basemodel import Timestamp


class Product(Timestamp):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='images/product/', default=None, blank=True)
    price = models.FloatField(default=0)
    on_discount = models.BooleanField(default=False)
    discount_price = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    description = models.TextField(default=None, blank=True)
    category = models.ManyToManyField('Category', related_name='products')
    tag = models.ManyToManyField('Tag', related_name='products', blank=True)

    def __str__(self):
        return self.name
