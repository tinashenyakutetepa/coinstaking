from django.urls import path, include
from .views import *

#investments Urls
urlpatterns = [    
    path('', investments, name='investment-list'),  
    path('test/', stake, name='test'),
    path('create/', create_orders, name='create'),  
    path('notification-status/', notification_status, name='n-status'),  
    path('success/', success_view, name='success'), 
]
