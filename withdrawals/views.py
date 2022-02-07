from django.shortcuts import render

# Withdrawals Views Here
def withdrawals_view(request):
    return render(request, 'withdrawals/withdrawals.html')
