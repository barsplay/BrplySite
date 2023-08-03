from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "price", "is_auction", "created_date"]
    actions = ["make_auction_as_true", "make_auction_as_false"]
    list_filter = ["is_auction", "created_at"]

    fieldsets = (
        ("Общее", {"fields": ("title", "description")}),
        ("Финансы", {"fields": ("price", "is_auction")})
    )

    @admin.action
    def make_auction_as_true(self, request, queryset):
        queryset.update(is_auction = True)

    @admin.action
    def make_auction_as_false(self, request, queryset):
        queryset.update(is_auction = False)


admin.site.register(Advertisement, AdvertisementAdmin)