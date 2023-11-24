from django import forms
from .models import location

class PuntoForm(forms.ModelForm):
    class Meta:
        model = location
        fields = ['name','adress','state','lat', 'lng', ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'lat': forms.TextInput(attrs={'class': 'form-control'}),
            'lng': forms.TextInput(attrs={'class': 'form-control'}),
        }