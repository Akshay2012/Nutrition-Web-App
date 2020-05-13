from .models import food
from django.forms import ModelForm

        
from .models import food,profile
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class food_form(ModelForm):
    class Meta:
        model=food
        fields=["food_name"]



class user_register(UserCreationForm):
    email=forms.EmailField(required=True)


    class Meta:
        model=User
        fields=["username","email","password1","password2",]


class update_profile_form(forms.ModelForm):

    class Meta:
        model=profile
        fields=['image','goal','goalweight','weight','activity_level','email']

  
class update_user_form(forms.ModelForm):

    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email'] 
