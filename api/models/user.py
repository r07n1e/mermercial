from django.db import models
from .basemodel import BaseModel


class User(BaseModel):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
