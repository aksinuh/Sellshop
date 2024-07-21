from django.urls import path
from .views import single_blog, single_product, blog, product_list,home
urlpatterns = [
    path("",home, name="home"),
    path("blog/",blog, name="blog"),
    path("single_product/",single_product, name="single_product"),
    path("product_list/",product_list, name="product_list"),
    path("single_blog/",single_blog, name="single_blog"),
]