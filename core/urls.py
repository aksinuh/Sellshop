from django.urls import path
from .views import about, contact_us, error_404, submit_contact
urlpatterns = [
    path("about/",about, name="about"),
    path("contact_us/",contact_us, name="contact_us"),
    path("error_404/",error_404, name="error_404" ), 
    path('submit_contact/', submit_contact, name='submit_contact'),
]