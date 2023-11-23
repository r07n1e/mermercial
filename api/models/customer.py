from django.db import models
from .basemodel import BaseModel


class Customer(BaseModel):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    nickname = models.CharField(max_length=255)
    password = models.TextField()

    def __str__(self):
        return self.name
