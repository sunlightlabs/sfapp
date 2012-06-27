from django import forms
from django.contrib.localflavor.us.forms import USZipCodeField

class SignupForm(forms.Form):
    email = forms.CharField(required=True, max_length=64)
    zipcode = forms.USZipCodeField(required=False)

