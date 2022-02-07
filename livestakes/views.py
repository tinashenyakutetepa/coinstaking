from django.shortcuts import render

# Livestake Views Here
def liveStake_view(request):
    return render(request, 'livestakes/live-feed.html')
