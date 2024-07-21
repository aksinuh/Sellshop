from django.contrib import admin
from .models import ContactUs, About, CreativeTeams
# Register your models here.


@admin.register(ContactUs)
class ContactUsadmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "message"]
    list_display_links = ["name"]
    
    
@admin.register(About)
class Aboutadmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]
    list_display_links = ["title"]
    
@admin.register(CreativeTeams)
class CreativeTeamsadmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]