from django import forms
from .models import TikaCard

class TikaCardForm(forms.ModelForm):
    class Meta:
        model = TikaCard
        fields = ['recipient_name', 'message', 'image', 'theme']
        widgets = {
            'recipient_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Recipient Name'}),
            'message': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write your Tika message', 'rows':4}),
            'theme': forms.Select(attrs={'class':'form-select'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
        }
