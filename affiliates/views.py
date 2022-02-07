from django.shortcuts import render
from .models import Affiliates

# Affiliates Views Here
def affiliates_view(request):
    downliner_bonus = Affiliates.objects.filter(benefiter = request.user)

    context = {
        'bonuses':downliner_bonus,
    }
    return render(request, 'affiliates/affiliates-list.html', context)
