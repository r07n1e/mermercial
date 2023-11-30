from django.db import models
from .basemodel import Timestamp
import uuid


class Customer(Timestamp):
    id = models.UUIDField(default=uuid.uuid4,
                          auto_created=True, serialize=False, verbose_name='ID', primary_key=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=254)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CustomerAddress(Timestamp):
    customer_id = models.ForeignKey(
        Customer, related_name='customer_address', on_delete=models.CASCADE)
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    postal_code = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
