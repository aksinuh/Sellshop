from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")

def order_complete(request):
    return render(request, "order-complete.html")

def wishlist(request):
    return render(request, "wishlist.html")