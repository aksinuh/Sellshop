from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request,"about.html")

def contact_us(request):
    return render(request,"contact.html")

def error_404(request):
    return render(request,"error-404.html")