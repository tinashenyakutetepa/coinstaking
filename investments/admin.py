from re import I
from django.contrib import admin
from .models import *

# Register investments models here.
admin.site.register(Investment)
admin.site.register(Bank)