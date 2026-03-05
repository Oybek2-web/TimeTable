from django import forms
from .models import Magazin, Profil

class MagazinForms(forms.ModelForm):
    class Meta:
        model = Magazin
        fields = '__all__'
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }


class ProfilForms(forms.ModelForm):
    class Meta:
        model = Profil
        fields = '__all__'
        widgets = {
            'profil_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'about_you': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }