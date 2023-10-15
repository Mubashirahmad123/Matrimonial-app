from django import forms
from django.forms import ModelForm
from .models import profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    subject = forms.CharField(max_length=100, widget=forms.Textarea)

    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = "__all__"

        # fields = ['name', 'age', 'gender', 'occupation']
        exclude=['profile_pic', 'date_of_birth', 'religion',\
                 ]



class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


       



    
