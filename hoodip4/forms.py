from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Posts,Business,Neighborhood

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_name', 'bio', 'profile_picture','neighborhood','location']  

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude =['user']
             
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user']    

class HoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['user']                  