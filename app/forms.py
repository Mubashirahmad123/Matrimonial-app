from django import forms
from django.forms import ModelForm
from .models import profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message






class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    subject = forms.CharField(max_length=100, widget=forms.Textarea)

    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = "__all__"

        # fields = ['name', 'age', 'gender', 'occupation']
        exclude=[ 'date_of_birth', 'user',
                 ]



class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


       






class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'message']


