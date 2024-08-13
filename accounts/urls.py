from django.urls import path, re_path
from .views import login, my_account,activate, logout
urlpatterns = [
    path("login/",login, name="login"),
    path("logout", logout, name= "logout"),
    path("my_account/",my_account, name="my_account"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,40})/$',
    activate, name='activate'),
    
]