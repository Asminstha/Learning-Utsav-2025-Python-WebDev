from django.shortcuts import render
from .models import Quote
import random

def home(request):
    quotes = Quote.objects.all()
    quote = random.choice(quotes) if quotes else None
    return render(request, 'home.html', {'quote': quote})
