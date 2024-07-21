from django.contrib import admin
from .models import (
    TimeStamp, Wishlist, Cart, Order,
    ShippingHanding, BllingDetails,
    City, State, Country, DifferentAddress
    
)

# Register your models here.

admin.site.register(TimeStamp)


@admin.register(Wishlist)
class Wishlistadmin(admin.ModelAdmin):
    list_display = ["id", "product", "user"]
    list_display_links = ["user"]
    
@admin.register(Cart)
class Cartadmin(admin.ModelAdmin):
    list_display = ["id", "product", "user", "quantity","shipping"]
    list_display_links = ["user"]
    
    
@admin.register(ShippingHanding)
class ShippingHandingadmin(admin.ModelAdmin):
    list_display = ["id", "shipping"]
    list_display_links = ["shipping"]
    
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
    list_display = ["id", "user", "product", "order_no", "blling", "cart"]
    list_display_links = ["user"]