from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_quote, name='add'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('ajax/toggle-like/', views.toggle_like, name='toggle_like'),
    path('ajax/increment-view/', views.increment_view, name='increment_view'),
]
