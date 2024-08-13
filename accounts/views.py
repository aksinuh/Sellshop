from django.shortcuts import render,redirect
from .forms import RegistrationForm, LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.contrib import messages
from django.contrib.auth import get_user_model

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

User = get_user_model()

# Create your views here.
def login(request):
    if request.method == "POST":
        if 'login_submit' in request.POST:
            login_form = LoginForm(data=request.POST)
            register_form = RegistrationForm()  # Register formu yenidən yaradılır
            if login_form.is_valid():
                user = authenticate(
                    request=request, email=login_form.cleaned_data["email"], password=login_form.cleaned_data["password"]
                )
                if user is not None:
                    django_login(request, user)
                    return redirect(reverse_lazy("home"))
                else:
                    messages.error(request, "User was not found!")
            else:
                messages.error(request, "Login form is not valid")
        
        elif 'register_submit' in request.POST:
            login_form = LoginForm()  # Login formu yenidən yaradılır
            register_form = RegistrationForm(data=request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.set_password(register_form.cleaned_data["password"])
                user.is_active = False
                user.save()

                current_site = get_current_site(request)
                subject = 'Activate Your MySite Account'
                message = render_to_string('account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                user.email_user(subject, message)
                messages.success(request, "Please confirm your email to complete the registration")
                return redirect(reverse_lazy('login'))
            else:
                messages.error(request, "Registration form is not valid")

    else:
        login_form = LoginForm()
        register_form = RegistrationForm()

    context = {
        'register_form': register_form,
        'login_form': login_form,
    }
    
    return render(request, "login.html", context=context)

def my_account(request):
    return render(request, "my-account.html")


def logout(request):
    django_logout(request)
    return redirect(reverse_lazy("login"))


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        django_login(request, user)
        return redirect('login')
    else:
        
        return redirect(reverse_lazy("login"))
        