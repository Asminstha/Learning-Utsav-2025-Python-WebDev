from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, default="My Shop")
    logo = models.ImageField(upload_to="logo/", blank=True, null=True)
    primary_color = models.CharField(max_length=7, default="#0d6efd")
    secondary_color = models.CharField(max_length=7, default="#6c757d")
    accent_color = models.CharField(max_length=7, default="#ffc107")
    hero_text = models.CharField(max_length=255, blank=True)
    footer_text = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    map_embed_url = models.TextField(blank=True, null=True)
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    



    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Site Settings"


class AboutUs(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    subtitle = models.CharField(max_length=300, blank=True)
    content = RichTextField(blank=True)  
    image = models.ImageField(upload_to="about/", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Us Section"

class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, help_text="Use emoji or Bootstrap icon class")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True, help_text="Bootstrap icon class or font-awesome class")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

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


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.client_name




class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="team/")
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name




