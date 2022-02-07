from django.urls import path, include
from .views import *

#interest Urls
urlpatterns = [    
    path('', interest_view, name='interest-list'),    
]
