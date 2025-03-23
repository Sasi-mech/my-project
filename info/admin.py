from django.contrib import admin
from .models import Club, ClubImage

class ClubImageInline(admin.TabularInline):
    model = ClubImage
    extra = 1

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    inlines = [ClubImageInline]

@admin.register(ClubImage)
class ClubImageAdmin(admin.ModelAdmin):
    pass