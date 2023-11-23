from django.db import models
from .basemodel import BaseModel


class Customer(BaseModel):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CustomerAddress(BaseModel):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_line1 = models.TextField()
    address_line2 = models.TextField()
    postal_code = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
