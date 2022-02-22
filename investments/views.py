import json
import requests
from django.shortcuts import render, redirect

from userProfile.models import User_profile
from .forms import stake_payment_form
from django.contrib import messages
from pycoingecko import CoinGeckoAPI
from .models import Investment, Bank
import uuid
from decimal import Decimal
from affiliates.models import Affiliates
from interests.models import Rate

from alfacoins_api_python import ALFACoins
from django.http import HttpResponse, JsonResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.csrf import csrf_exempt


# investments views here.
alfacoins = ALFACoins(
    name='Crypto Coin Staking',
    password='BTj9G3!kfubMEud',
    secret_key='b502070e80698ba490ec6350e291e16f'
    )

@xframe_options_sameorigin
def create_orders(request):    
    amount = request.session.get('amount')
    ref = request.session.get('ref')
    
    
    result = alfacoins.create_order(
    type='litecointestnet',
    amount= amount,
    currency='LTCT',
    order_id= ref, #ref,   
    options={                  
        'notificationURL': 'https://app.datlabeswatini.co/investments/notification-status/',
        'redirectURL': 'https://app.datlabeswatini.co/investments/success',
        'payerName': 'Bob',
        'payerEmail': 'no_reply@alfacoins.com', 
        #'test':1,
	    #'status':'completed'       
            },
    description='Staking investment',   
    ) 

    context = {
        'result':result,
    }
    return render(request, 'investments/stack.html', context) 
    

def investments(request):
    stakes = Investment.objects.filter(user = request.user)
    
    context = {        
        'stakes':stakes,
    }
    return render(request, 'investments/investments-list.html', context)

def stake(request):
    
    cg = CoinGeckoAPI()
    p = cg.get_price(ids=['dogecoin'], vs_currencies='usd')
    doge = "{:.2f}".format(20 / p['dogecoin']['usd'])
    dogerate = Decimal(p['dogecoin']['usd'])
    ref = str(uuid.uuid4()).replace("-", "")[:6]  

    form = stake_payment_form()
    if request.method == 'POST':
        form = stake_payment_form(request.POST or None, request.FILES or None)
        
               

        if form.is_valid():
            doge_amount = form.cleaned_data.get('amount_in_doge')
            current_usd_amount = doge_amount * dogerate
            obtain_total = Bank.objects.get(user = request.user)
            available_amount = obtain_total.total_coins
                     

            instance = form.save(commit=False)
            instance.user = request.user
            instance.invstmt_ref = ref 
            instance.amount_in_usd = current_usd_amount  
            user_bank = Bank.objects.get(user = instance.user)          
            user_bank.total_coins = available_amount + instance.amount_in_doge

            #Affiliate bonus
            me = User_profile.objects.get(user = instance.user)
            benefiter = me.recommended_by          
            
            try:
                check = Affiliates.objects.get(user=instance.user)
                if check is not None:                    
                    pass
            except:                  
                fixed_rate = Rate.objects.get()
                rate = fixed_rate.affiliate_rate
                todays_interest_doge = rate / 100 * doge_amount

                Affiliates.objects.create(
                    user = instance.user,
                    benefiter = benefiter,
                    amount = todays_interest_doge
                )     
            
            user_bank.save()                       
            instance.save()            
            messages.success(request, 'Investment scheduled')
           
            request.session['amount'] = str(doge_amount)
            request.session['ref'] = instance.invstmt_ref
            return redirect('create')

    context = {
        'form': form, 
        'dogecoin':doge,       
    }
    return render(request, 'investments/test.html', context)


@csrf_exempt
def notification_status(request, *args, **kwargs):       
    print('Initial Notification')
    if request.method=='POST':    
        try:
            data=json.loads(request.body)
            id = data['order_id']
            status = data['status']
            print(data, id, status)             
            Investment.objects.filter(invstmt_ref = id).update(
                status = status
            )
        except: 
            print('No Notification')
            return JsonResponse(data)             
    return HttpResponse("Done")

      

def success_view(request):
   
    context = {
         
        'msg':'Investment Successfull',       
    }
    return render(request, 'investments/success.html', context)
