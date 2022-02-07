from django.shortcuts import render

# Contact us Views Here
def contactUs_view(request):
    return render(request, 'contactUs/contact-us.html')
