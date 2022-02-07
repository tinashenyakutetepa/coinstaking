from re import T
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Affiliates models here.

class Affiliates(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    benefiter = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='benefiter')
    amount = models.DecimalField(max_digits = 15, decimal_places = 2, null=False, blank=True,)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)