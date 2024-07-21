from django.db import models
from products.models import ProductDetail
from django.contrib.auth import get_user_model
# Create your models here

User = get_user_model()


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wishlist(models.Model):
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE, related_name="wishlist_product")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wish_user")
    
    
class Cart(models.Model):
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE, related_name="cart_product")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart_user")
    quantity = models.IntegerField()
    shipping = models.ForeignKey("ShippingHanding", on_delete=models.CASCADE, related_name="cart_shipping")
    
class ShippingHanding(models.Model):
    shipping = models.DecimalField(max_digits=10, decimal_places=2)
    

class BllingDetails(models.Model):
    name = models.CharField(max_length=50)
    enter_your_here = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    country = models.ForeignKey("Country", on_delete=models.CASCADE)
    state = models.ForeignKey("State", on_delete=models.CASCADE)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    
    
class City(models.Model):
    name  = models.CharField(max_length=100)
    
    
class State(models.Model):
    name = models.CharField(max_length=100)
        
        
class Country(models.Model):
    name = models.CharField(max_length=100)


class DifferentAddress(models.Model):
    name = models.CharField(max_length=50)
    enter_your_here = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    note = models.TextField()

class Order(TimeStamp):
    product = models.ForeignKey(ProductDetail , on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_no = models.IntegerField()
    blling = models.ForeignKey(BllingDetails, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
