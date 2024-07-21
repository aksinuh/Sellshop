from django.urls import path
from .views import login, my_account
urlpatterns = [
    path("login/",login, name="login"),
    path("my_account/",my_account, name="my_account"),
    
]