from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False
            user.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            domain = get_current_site(request).domain
            link = f"http://{domain}/users/activate/{uid}/{token}/"
            message = render_to_string('users/activation_email.html', {'link':link,'user':user})
            send_mail('Activate your InspireVerse account', message, None, [user.email])
            messages.success(request, "Account created successfully!")
            return render(request,'users/please_confirm.html')
        else:
            messages.error(request, "There was an error in your registration. Please check the form.")
    else:
        form = RegisterForm()
    return render(request,'users/register.html',{'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception:
        user = None
    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request,user)
        return redirect('quotes:home')
    return render(request,'users/activation_invalid.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username,password=password)
        if user:
            login(request,user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('quotes:home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request,'users/login.html')

def user_logout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('quotes:home')
