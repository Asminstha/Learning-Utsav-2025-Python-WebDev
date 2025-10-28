from django.contrib import admin
from .models import AboutUs , Feature
from .models import SiteSettings, Service, GalleryImage, ContactMessage , Testimonial, TeamMember

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




@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'created_at')
    search_fields = ('client_name', 'message')
    list_filter = ('created_at',)

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')

