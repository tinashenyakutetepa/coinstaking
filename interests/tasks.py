from django.contrib.auth import get_user_model
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Interest, Rate, Interest_Bank
from decimal import Decimal
from investments.models import Bank
from pycoingecko import CoinGeckoAPI


@shared_task(bind=True)
def update_interest(self):    
    User = get_user_model()
    users = User.objects.all()

    #Interest
    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['dogecoin'], vs_currencies='usd')

    for user in users:

        #Interest        
        obtain_total = Bank.objects.get(user = user)
        available_amount_doge = obtain_total.total_coins
        dogerate = Decimal(p['dogecoin']['usd'])

        fixed_rate = Rate.objects.get()
        rate = fixed_rate.rate
        todays_interest_doge = rate / 100 * available_amount_doge                
        todays_interest_usd = "{:.4f}".format(todays_interest_doge * dogerate)

        
        Interest.objects.create(
            user = user,
            investment_amount = available_amount_doge,            
            interest_per_day = rate,
            interest_doge = todays_interest_doge, 
            interest_usd = todays_interest_usd,
        )

        get_object = Interest_Bank.objects.get(user = user)
        coins = get_object.total_interest_coins
        print(coins)
        Interest_Bank.objects.filter(user = user).update(            
            total_interest_coins = coins + todays_interest_doge
        )
    return "Done"
