from django.http import HttpResponse
from django.shortcuts import render 
# creating function
def home(request):
    return render(request , 'home.html')