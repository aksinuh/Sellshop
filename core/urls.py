from django.urls import path
from .views import about, contact_us, error_404
urlpatterns = [
    path("about/",about, name="about"),
    path("contact_us/",contact_us, name="contact_us"),
    path("error_404/",error_404, name="error_404" ),
    
]