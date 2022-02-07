from django.urls import path, include
from .views import *

#Livestakes Urls
urlpatterns = [    
    path('', withdrawals_view, name='withdrawals'),    
]
