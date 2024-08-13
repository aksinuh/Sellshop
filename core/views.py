from django.shortcuts import render
from .models import About,CreativeTeams
# Create your views here.

def about(request):
    about = About.objects.first()
    creative = CreativeTeams.objects.all()
    context = {
        'about': about,
        'creative': creative
    }
    return render(request,"about.html", context=context)

def contact_us(request):
    return render(request,"contact.html")

def error_404(request):
    return render(request,"error-404.html")

