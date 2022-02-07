from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


# interest models here.

class Rate(models.Model):
    rate = models.DecimalField(max_digits = 15, decimal_places = 2, null=False, blank=True,)
    affiliate_rate = models.DecimalField(max_digits = 15, decimal_places = 2, null=False, blank=True,)
    
    def __str__(self):
        return str(self.rate)

class Interest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    investment_amount = models.DecimalField(max_digits = 15, decimal_places = 2, null=True, blank=True,)
    interest_per_day = models.DecimalField(max_digits = 15, decimal_places = 2, null=True, blank=True,)
    interest_doge = models.DecimalField(max_digits = 15, decimal_places = 2, null=True, blank=True,)
    interest_usd = models.DecimalField(max_digits = 15, decimal_places = 2, null=True, blank=True,)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username +" | "+ str(self.investment_amount) 
    
class Interest_Bank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_interest_coins = models.DecimalField(max_digits = 15, decimal_places = 2, default=0, null=True, blank=True,)

    def __str__(self):
        return self.user.username + " | " + self.user.email + " | " + str(self.total_interest_coins)
