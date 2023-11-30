from django.db import models
from .basemodel import Timestamp
from django.contrib.auth.models import User
import uuid


class Coupon(Timestamp):
    code = models.CharField(max_length=254)
    description = models.TextField()
    discount_value = models.DecimalField(max_digits=100, decimal_places=2)
    discount_type = models.CharField(max_length=254)
    time_used = models.IntegerField()
    max_usage = models.IntegerField()
    coupon_start_date = models.DateTimeField()
    coupon_end_date = models.DateTimeField()
    created_by = models.ForeignKey(
        User, related_name='coupons', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
