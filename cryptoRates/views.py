from django.shortcuts import render

# Crypto Rates Views Here
def cryptoRates_view(request):
    return render(request, 'cryptoRates/crypto-rates.html')
