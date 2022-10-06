import email
from django import forms
from accounts.models import Account
from django.contrib.auth.forms import UserCreationForm

class playerForm(UserCreationForm):
    email=forms.EmailField(max_length=50)
    class Meta:
        model = Account
        fields= ('username','email','first_name','last_name','image','position','kit_number','password1','password2')