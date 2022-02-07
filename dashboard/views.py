from django.shortcuts import render
from django.contrib.auth.models import User
from userProfile.models import User_profile
from pycoingecko import CoinGeckoAPI
from decimal import Decimal
from investments.models import Bank
from interests.models import Rate, Interest_Bank
from affiliates.models import Affiliates
from django.db.models import Sum

# Dashboard Views Here
def dashboard_view(request):
    
    #downliners 
    user = request.user
    downliners = User_profile.objects.filter(recommended_by = user)
    
    #Live Crypto rates from coingeckoapi
    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum', 'gamecredits','neo','dnotes', 'mintcoin', 'iotex', 'dash', 'steem', 'lbry-credits', 'dogecoin'], vs_currencies='usd')
    lbc = p['lbry-credits']['usd']
     
    #Total coins Available
    obtain_total = Bank.objects.get(user = request.user)
    available_amount_doge = obtain_total.total_coins
    dogerate = Decimal(p['dogecoin']['usd'])
    available_amount_usd = "{:.2f}".format(available_amount_doge * dogerate)

    #Interest
    fixed_rate = Rate.objects.get()
    rate = fixed_rate.rate
    interest_user = Interest_Bank.objects.get(user = request.user)
    interest_availbale = interest_user.total_interest_coins
    todays_interest_doge = interest_availbale              
    todays_interest_usd = "{:.4f}".format(todays_interest_doge * dogerate)

    #Wallet Ballance
    balance = "{:.2f}".format(Bank.objects.all().aggregate(Sum('total_coins'))['total_coins__sum'])
    users = User.objects.all().count()

    #Affiliates   
    try:
        bonuses = Affiliates.objects.filter(benefiter = request.user).aggregate(Sum('amount'))['amount__sum']      
        bonus_in_doge = "{:.3f}".format(bonuses)
        bonus_in_usd = "{:.2f}".format(Decimal(bonus_in_doge) * dogerate)
    except:

        bonus_in_doge = 0
        bonus_in_usd = 0

            
    context = {
        'downliners': downliners,
        'bonus':bonus_in_doge,
        'bonus_usd':bonus_in_usd,
        'price':p,
        'lbc':lbc,
        'mycoins':available_amount_doge,
        'myusd': available_amount_usd,
        'todays_interest_doge':todays_interest_doge,
        'todays_interest_usd':todays_interest_usd,
        'balance':balance,
        'users':users,
       }
    return render(request, 'dashboard/dashboard.html', context)


