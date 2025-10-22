from django.db import models
from django.contrib.auth.models import User
import uuid

class TikaCard(models.Model):
    THEME_CHOICES = [
        ('classic', 'Classic Red & Gold'),
        ('modern', 'Modern Vibrant'),
        ('fun', 'Fun & Colorful'),
    ]

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient_name = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    image = models.ImageField(upload_to='cards/', blank=True, null=True)
    theme = models.CharField(max_length=20, choices=THEME_CHOICES, default='classic')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.creator.username} → {self.recipient_name}"
