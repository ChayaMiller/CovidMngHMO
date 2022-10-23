from django import forms  
from django.forms import ModelForm
from .models import Patient,Vaccine

class CreateForm(forms.ModelForm):  
    class Meta:  
        model = Patient  
        fields = "__all__" 

class CreateVacForm(forms.ModelForm):  
    class Meta:  
        model = Vaccine  
        fields = "__all__" 