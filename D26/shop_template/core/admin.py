from django.contrib import admin
from .models import AboutUs , Feature
from .models import SiteSettings, Service, GalleryImage, ContactMessage

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name",)


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("title", "updated_at")

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("title", "order")

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    ordering = ("order",)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "added_at")

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "handled")
    list_filter = ("handled",)
