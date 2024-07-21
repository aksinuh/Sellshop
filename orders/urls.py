from django.urls import path
from .views import cart, order_complete, checkout,wishlist
urlpatterns = [
    path("cart/",cart, name="cart"),
    path("order_complete/",order_complete, name="order_complete"),
    path("checkout/", checkout, name="checkout"),
    path("wishlist/",wishlist, name="wishlist"),
]