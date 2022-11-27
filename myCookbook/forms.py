from .models import User
from django import forms

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','email','password','bio','theme','profile_image') 
        widgets = {'username':forms.TextInput(attrs={'class': 'form-control','placeholder':"Username"}),
        'password':forms.PasswordInput(attrs={'class': 'form-control','placeholder':"Password","required": True}),
        'email':forms.TextInput(attrs={'class': 'form-control','placeholder':"Email","required": True}),
        'bio':forms.Textarea(attrs={'class': 'form-control','placeholder':"Share a bit about yourself!"}),
        'theme':forms.Select(attrs={'class': 'form-control', "required": True}),
        'profile_image':forms.FileInput(attrs={'class': 'form-control-file'}),
        }
