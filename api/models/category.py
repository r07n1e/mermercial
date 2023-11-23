from django.db import models
from .basemodel import BaseModel
import uuid


class Category(BaseModel):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='images/category', default=None, blank=True)
    active = models.BooleanField(default=False)
    description = models.TextField(default=None, blank=True)

    def __str__(self):
        return self.name
