from django import forms
from .models import ReceiptModel, SearchModel


class ReceiptForm(forms.Form):
    img = forms.ImageField(label='', required=False)
    model = ReceiptModel
    fields = ('image',)
    # widgets = {
    #         'myfield': forms.FileInput(attrs={'class': 'icons'}),
    #     }
    
    print("Image Form")


class SearchForm(forms.Form):
    item = forms.CharField(label='', required=False)
    model = SearchModel
    fields = ('text',)


