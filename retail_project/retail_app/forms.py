# iris_app/forms.py
from django import forms

class RetailForm(forms.Form):
    UnitPrice = forms.FloatField(label='Prix unitaire')
   
