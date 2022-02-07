from django.forms import ModelForm
from django import forms
from .models import *

 
#applications Forms

class DateInput(forms.DateInput):
    input_type = 'date'

class stake_payment_form(forms.ModelForm):
       
     class Meta:
        model = Investment
        fields = '__all__'
        exclude = ['user', 'invstmt_number', 'amount_in_usd']
          
        widgets = {
            'amount_in_doge' : forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Amount'}),            
            }       
    