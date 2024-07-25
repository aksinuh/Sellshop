from django.contrib import admin
from .models import (
    Wishlist, Cart, Order,
     BllingDetails,
    City, State, Country, DifferentAddress
    
)

# Register your models here.




@admin.register(Wishlist)
class Wishlistadmin(admin.ModelAdmin):
    list_display = ["id", "user"]
    list_display_links = ["user"]
    
@admin.register(Cart)
class Cartadmin(admin.ModelAdmin):
    list_display = ["id",  "user"]
    list_display_links = ["user"]
    
    
@admin.register(BllingDetails)
class BllingDetailsadmin(admin.ModelAdmin):
    list_display = ["id", "name", "enter_your_here", "company_name", "state","city", "address"]
    list_display_links = ["name"]
    
    
@admin.register(City)
class Cityadmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]
    
    
@admin.register(State)
class Stateadmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]
    
    
    
@admin.register(Country)
class Countryadmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]
    
    
@admin.register(DifferentAddress)
class DifferentAddressadmin(admin.ModelAdmin):
    list_display = ["id", "name", "enter_your_here", "company_name", "state","city", "note"]
    list_display_links = ["name"]
    

@admin.register(Order)
class Orderadmin(admin.ModelAdmin):
    list_display = ["id", "user", "order_no", "blling", "cart"]
    list_display_links = ["user"]