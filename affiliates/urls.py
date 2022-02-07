from django.urls import path, include
from .views import *

#Affiliates Urls
urlpatterns = [    
    path('', affiliates_view, name='affiliates-list'),    
]
