from django.db import models
from .basemodel import Timestamp


class Tag(Timestamp):
    name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
