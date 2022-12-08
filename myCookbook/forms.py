from .models import User, Recipe, Category, Review
from django import forms
from django.contrib.auth.forms import PasswordResetForm


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',
                  'bio', 'theme', 'profile_image')
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username", "required": True}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "First Name", "required": True}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Last Name", "required": True}),
                   'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password", "required": True}),
                   'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Email", "required": True}),
                   'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Share a bit about yourself!"}),
                   'theme': forms.Select(attrs={'class': 'form-control', "required": True}),
                   'profile_image': forms.FileInput(attrs={'class': 'form-control-file'}),
                   }


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name','categories', 'description', 'num_servings',
                  'min', 'image', 'instructions')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Name"}),
                   'categories': forms.CheckboxSelectMultiple(),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Description"}),
                   'num_servings': forms.NumberInput(attrs={'class': 'form-control'}),
                   'min': forms.NumberInput(attrs={'class': 'form-control'}),
                   'image': forms.FileInput(attrs={'class': 'form-control-file', "name": 'image'})
                   }


class MyPasswordResetForm(PasswordResetForm):
    def is_valid(self):
        email = self.data["email"]
        return super().is_valid()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('subject', 'review','rating',)