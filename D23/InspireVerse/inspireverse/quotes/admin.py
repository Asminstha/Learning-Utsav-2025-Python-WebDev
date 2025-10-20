from django.contrib import admin
from .models import Quote, SiteStat

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('short_text','author','approved','created_at','like_count')
    list_filter = ('approved','created_at')
    search_fields = ('text','quoted_by','author__username')
    actions = ['approve_quotes','disapprove_quotes']

    def short_text(self,obj):
        return obj.text[:60]
    short_text.short_description = 'Quote'

    def approve_quotes(self, request, queryset):
        queryset.update(approved=True)
    approve_quotes.short_description = "Mark selected quotes as approved"

    def disapprove_quotes(self, request, queryset):
        queryset.update(approved=False)
    disapprove_quotes.short_description = "Mark selected quotes as disapproved"

admin.site.register(SiteStat)
