from django.contrib import admin
from main.models import Main, Hero, Blog
# Register your models here.
@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('logo',)

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'short_description' , 'views', 'image', 'transcription')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','photo','published_at')