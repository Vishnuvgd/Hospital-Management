from django import forms
from .models import *

# class DateInput(forms.DateInput):
#     input_type = 'date'
#
# class Bookingform(forms.ModelForm):
#     class Meta:
#         model=bookingmodel
#         fields='__all__'
#
#     widgets = {'booking_date': DateInput()}

class bookingform(forms.Form):
    p_name=forms.CharField(max_length=20)
    p_phone=forms.CharField(max_length=10)
    p_email=forms.EmailField()
    doc_name=forms.CharField(max_length=20)
    booking_date=forms.DateField()