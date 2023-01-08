from django import forms
from app.models import *

class RegistrationForm(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}


class Profile(forms.ModelForm):
    class Meta():
        model=Registration
        fields=['address','profile_pic']