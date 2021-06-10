from django import forms
from django.forms import ModelForm
from .models import ShoppingItem

class ShoppingForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields=['title','quantity','store','purchased']
      
         
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter shopping item...",}),)
    
    quantity = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter quantity...",}),)
    
    store = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter store name...",}),)
    
    purchased = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(attrs={"class": "form-check-input"}),
    )
       