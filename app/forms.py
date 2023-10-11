from django import forms
from django.forms import ModelForm
from .models import profile




class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    subject = forms.CharField(max_length=100, widget=forms.Textarea)

    

class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = "__all__"


    
