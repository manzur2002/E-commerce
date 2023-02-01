from django import forms
from .models import Order


class OrderForm(forms.Form):
    full_name = forms.CharField( label='Write your address')
    address = forms.CharField( label='Write your address')
    phone = forms.CharField( label='Write your phone')

    class Meta:
        model = Order
        fields = ['full_name',  'address', 'phone']


