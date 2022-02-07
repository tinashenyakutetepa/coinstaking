from django.shortcuts import render
from .models import Interest

# Interest Views Here
def interest_view(request):    
   
    daily_interests = Interest.objects.filter(user = request.user, investment_amount__gt = 0)
    context = {
        'interests':daily_interests,
    }
    return render(request, 'interests/interests-list.html', context)


