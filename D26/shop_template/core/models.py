from django.db import models
from django.utils import timezone

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default="My Shop")
    logo = models.ImageField(upload_to="logo/", blank=True, null=True)
    primary_color = models.CharField(max_length=7, default="#0d6efd")
    secondary_color = models.CharField(max_length=7, default="#6c757d")
    accent_color = models.CharField(max_length=7, default="#ffc107")
    hero_text = models.CharField(max_length=255, blank=True)
    footer_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "Site Settings"

    class Meta:
        verbose_name_plural = "Site Settings"

class Page(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True, help_text="Bootstrap icon class or font-awesome class")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="gallery/")
    caption = models.CharField(max_length=255, blank=True)
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title or f"Image {self.pk}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    handled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject or 'Message'}"
