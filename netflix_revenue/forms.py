from django import forms
from .models import Customer

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'service_type', 'payment_method', 'duration', 'total_payment']
