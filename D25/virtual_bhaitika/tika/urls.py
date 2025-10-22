from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create-card/', views.create_card, name='create_card'),
    path('preview/<uuid:card_uuid>/', views.preview_card, name='preview_card'),
    path('delete-card/<uuid:card_uuid>/', views.delete_card, name='delete_card'),


]
