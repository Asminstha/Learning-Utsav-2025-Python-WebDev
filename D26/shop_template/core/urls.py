from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services_view, name="services"),
    path("gallery/", views.gallery_view, name="gallery"),
    path("contact/", views.contact, name="contact"),
]
