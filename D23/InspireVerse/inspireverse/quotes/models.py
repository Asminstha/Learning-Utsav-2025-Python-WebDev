from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Quote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quotes')
    text = models.TextField()
    quoted_by = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='liked_quotes', blank=True)
    views = models.PositiveIntegerField(default=0)

    def like_count(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.text[:50]}... by {self.quoted_by or self.author.username}"

class SiteStat(models.Model):
    # single-row model for site statistics
    home_visits = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"Visits: {self.home_visits}"

    class Meta:
        verbose_name_plural = 'Site statistics'
