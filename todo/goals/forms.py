from django import forms
from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields=['title','description','target_date','completed']
      
         
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter goal...",}),)
    
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter description...",}),)
    
    target_date = forms.DateField(
        required=False,
        widget=SelectDateWidget(),)
    

    completed = forms.CharField(
        required=False,
        widget=forms.widgets.CheckboxInput(attrs={"class": "form-check-input"}),
    )