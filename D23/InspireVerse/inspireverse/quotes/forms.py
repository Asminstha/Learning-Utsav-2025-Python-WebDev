from django import forms
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('text','quoted_by')
        widgets = {
            'text': forms.Textarea(attrs={'rows':3,'placeholder':'Write a quote...'}),
            'quoted_by': forms.TextInput(attrs={'placeholder':'Who said it? (optional)'}),
        }
