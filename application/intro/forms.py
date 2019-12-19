from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
from .models import ReceiptModel, SearchModel


class ReceiptForm(forms.Form):
    img = forms.ImageField(label='', required=False)
    model = ReceiptModel
    fields = ('image',)
    # widgets = {
    #         'myfield': forms.FileInput(attrs={'class': 'icons'}),
    #     }
    
    print("Image Form")

# class TableForm(form.Form):
#     tbl = forms.

class SearchForm(forms.Form):
    item = forms.CharField(label='', required=False)
    model = SearchModel
    fields = ('text',)


