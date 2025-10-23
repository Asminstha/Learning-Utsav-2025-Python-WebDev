from .models import SiteSettings
from django.utils import timezone

def global_settings(request):
    return {
        'settings': SiteSettings.objects.first(),
        'now': timezone.now(),
    }
