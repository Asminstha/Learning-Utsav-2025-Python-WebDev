from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quote, SiteStat
from .forms import QuoteForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.db import models as djmodels
from django.contrib import messages


def home(request):
    stat, _ = SiteStat.objects.get_or_create(pk=1)
    stat.home_visits = djmodels.F('home_visits') + 1
    stat.save()
    stat.refresh_from_db()
    quotes = Quote.objects.filter(approved=True).order_by('-created_at')
    return render(request,'quotes/home.html',{'quotes':quotes,'stat':stat})
@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.author = request.user  # assign the logged-in user here
            if request.user.is_superuser:
                quote.approved = True
            quote.save()
            if request.user.is_superuser:
                messages.success(request, "Quote posted successfully!")
            else:
                messages.success(request, "Quote submitted for approval.")
            return redirect('quotes:home')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    total = user.quotes.count()
    approved = user.quotes.filter(approved=True).count()
    disapproved = user.quotes.filter(approved=False).count()
    return render(request,'quotes/dashboard.html',{'total':total,'approved':approved,'disapproved':disapproved})

@require_POST
@login_required
def toggle_like(request):
    quote_id = request.POST.get('id')
    quote = get_object_or_404(Quote, pk=quote_id, approved=True)
    user = request.user
    if user in quote.likes.all():
        quote.likes.remove(user)
        liked = False
    else:
        quote.likes.add(user)
        liked = True
    return JsonResponse({'liked':liked,'like_count':quote.like_count()})

@require_POST
def increment_view(request):
    quote_id = request.POST.get('id')
    quote = get_object_or_404(Quote, pk=quote_id, approved=True)
    quote.views = djmodels.F('views') + 1
    quote.save()
    quote.refresh_from_db()
    return JsonResponse({'views': quote.views})
