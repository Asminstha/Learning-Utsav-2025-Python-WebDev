from django.urls import path, include
from .views import authView, home, logout_view

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="authView"),
    path("accounts/logout/", logout_view, name="logout"),  # ✅ custom logout route
    path("accounts/", include("django.contrib.auth.urls")),
]
