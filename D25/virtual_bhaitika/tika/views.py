from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TikaCard
from .forms import TikaCardForm
from django.contrib import messages 

# Home page
def home(request):
    return render(request, 'tika/home.html')

# Dashboard - only for logged-in users
@login_required
def dashboard(request):
    cards = TikaCard.objects.filter(creator=request.user).order_by('-created_at')
    return render(request, 'tika/dashboard.html', {'cards': cards})

# Create Card - only for logged-in users
@login_required
def create_card(request):
    if request.method == 'POST':
        form = TikaCardForm(request.POST, request.FILES)
        if form.is_valid():
            card = form.save(commit=False)
            card.creator = request.user
            card.save()
            return redirect('preview_card', card_uuid=card.uuid)
    else:
        form = TikaCardForm()

    # Always return a response
    return render(request, 'tika/create_card.html', {'form': form})

# Preview Card - anyone with link
def preview_card(request, card_uuid):
    card = get_object_or_404(TikaCard, uuid=card_uuid)
    return render(request, 'tika/preview_card.html', {'card': card})




@login_required
def delete_card(request, card_uuid):
    card = get_object_or_404(TikaCard, uuid=card_uuid, creator=request.user)
    if request.method == 'POST':
        card.delete()
        return redirect('dashboard')
    return render(request, 'tika/confirm_delete.html', {'card': card})
