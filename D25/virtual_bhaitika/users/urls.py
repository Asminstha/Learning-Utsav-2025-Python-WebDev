from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

class CustomLoginView(auth_views.LoginView):
    template_name = 'users/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
     path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
]
