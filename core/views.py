from django.shortcuts import render,redirect
from .models import About,CreativeTeams
from .forms import ContactUsForm
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib import messages
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

def submit_contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Uğurlu göndərmədən sonra yönləndirmə
    else:
        form = ContactUsForm()
    return render(request, 'base.html', {'contact_form': form})

