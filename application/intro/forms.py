from django import forms
from .models import ReceiptModel, SearchModel


class ReceiptForm(forms.Form):
    img = forms.ImageField(label='')
    model = ReceiptModel
    fields = ('image',)
    # widgets = {
    #         'myfield': forms.FileInput(attrs={'class': 'icons'}),
    #     }
    
    print("Image Form")


class SearchForm(forms.Form):
    item = forms.CharField(label='')
    model = SearchModel
    fields = ('text',)


