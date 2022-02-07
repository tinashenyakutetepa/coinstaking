from django.db.models.signals import post_save
from django.contrib.auth.models import User

from interests.models import Interest, Interest_Bank
from .models import User_profile
from investments.models import Bank
import uuid


#Profile signals

def user_profile(sender, instance, created, **kwargs):
    if created:       
        code = str(uuid.uuid4()).replace("-", "")[:12]
        User_profile.objects.create(
            user=instance,
            code=code            
            )
        Bank.objects.create(
            user = instance,
            total_coins = 0
        )
        Interest_Bank.objects.create(
            user = instance,
            total_interest_coins = 0
        )       
post_save.connect(user_profile, sender=User)