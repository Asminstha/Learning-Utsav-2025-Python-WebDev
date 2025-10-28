from django.shortcuts import render, redirect
from .models import SiteSettings, Service, GalleryImage , AboutUs , Feature ,Testimonial, TeamMember
from .forms import ContactForm
from django.contrib import messages

def get_site_settings():
    # Return the first settings instance or defaults
    s = SiteSettings.objects.first()
    return s

def home(request):
    settings = get_site_settings()
    services = Service.objects.all().order_by("order")
    gallery = GalleryImage.objects.all().order_by("-added_at")[:8]
    about_us = AboutUs.objects.first()   
    features = Feature.objects.all()    
    testimonials = Testimonial.objects.all()
    team_members = TeamMember.objects.all()
    context = {
        "settings": settings,
        "services": services,
        "gallery": gallery,
        "about_us": about_us,
        "features": features,
        "testimonials": testimonials,
        "team_members": team_members,
    }
    return render(request, "core/home.html", context)



def about(request):
    settings = get_site_settings()
    about_us = AboutUs.objects.first()
    features = Feature.objects.all()
    context = {
        "settings": settings,
        "about_us": about_us,
        "features": features,
    }
    return render(request, "core/about.html", context)

def services_view(request):
    settings = get_site_settings()
    services = Service.objects.all().order_by("order")
    return render(request, "core/services.html", {"settings": settings, "services": services})

def gallery_view(request):
    settings = get_site_settings()
    images = GalleryImage.objects.all().order_by("-added_at")
    return render(request, "core/gallery.html", {"settings": settings, "images": images})

def contact(request):
    settings = get_site_settings()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent. Thank you!")
            return redirect("contact")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()
    return render(request, "core/contact.html", {"settings": settings, "form": form})


def contact_view(request):
    site_settings = SiteSettings.objects.first()
    return render(request, "contact.html", {"site_settings": site_settings})