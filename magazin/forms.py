from django import forms
from .models import TimeTable, Profil

class TimeTableForms(forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = '__all__'
        widgets = {
            'kurs_nomi': forms.TextInput(attrs={'class': 'form-control'}),
            'auditoriya': forms.TextInput(attrs={'class': 'form-control'}),
            'start': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'finish': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'guruh': forms.TextInput(attrs={'class': 'form-control'}),
            'sana': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'created_at':forms.DateTimeField(),
        }

class ProfilForms(forms.ModelForm):
    class Meta:
        model = Profil
        exclude = ['user']
        widgets = {
            'profil_photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'about_you': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }