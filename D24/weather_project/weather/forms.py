from django import forms

class CityForm(forms.Form):
    city = forms.CharField(
        max_length=100, 
        label='Enter City Name', 
        widget=forms.TextInput(attrs={'placeholder': 'City Name', 'class': 'form-control'})
    )
