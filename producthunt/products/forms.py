from django import forms
from .models import Student

class MyForm(forms.Form):
    Name = forms.CharField(label='Enter your name', max_length=100)
    Email = forms.EmailField(label='Enter your email', max_length=100)
    Feedback = forms.CharField(widget=forms.Textarea(attrs={'width':"100%", 'cols' : "70", 'rows': "10", }))
    Card_Number = forms.CharField(label='Enter your card no', max_length=100)
