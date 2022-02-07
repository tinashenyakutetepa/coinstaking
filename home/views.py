from django.shortcuts import render

# Home Views Here
def home_view(request):
    return render(request, 'home/home.html')
