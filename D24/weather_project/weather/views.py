from django.shortcuts import render
import requests
from .forms import CityForm

API_KEY = 'b7371edf66a465727f98503e63ffee2c'

def home(request):
    weather_data = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon'],
                }
            elif response.status_code == 404:
                weather_data = {'error': 'City not found. Please check the spelling!'}
            else:
                weather_data = {'error': f"Error fetching data. Status code: {response.status_code}"}
    else:
        form = CityForm()

    return render(request, 'weather/home.html', {'form': form, 'weather_data': weather_data})
