from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# investment models here.

class Investment(models.Model):    

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invstmt_ref = models.CharField(max_length = 6, unique=True, blank=True, null=False)
    amount_in_usd = models.DecimalField(max_digits = 15, decimal_places = 2, null=False, blank=True,)
    amount_in_doge = models.DecimalField(max_digits = 15, decimal_places = 2, null=False, blank=True,)
    status = models.CharField(max_length = 10, default='Processing', blank=True, null=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email + " | " + str(self.amount_in_doge)
 
class Bank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_coins = models.DecimalField(max_digits = 15, decimal_places = 2, null=False, blank=True,)

    def __str__(self):
        return self.user.username + " | " + self.user.email + " | " + str(self.total_coins)