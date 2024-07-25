from django.shortcuts import render
from .models import  ProductDetail, Product,SingleBlog
# Create your views here.
def blog(request):
    blogs = SingleBlog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, "blog.html", context=context)

def product_list(request):
    return render(request, "product-list.html")

def single_blog(request, id):
    blog = SingleBlog.objects.get(id=id)
    
    context = {
        'blog': blog
    }
    return render(request, "single-blog.html", context=context)


def single_product(request, id):
    detail = ProductDetail.objects.get(id=id)
    
    context = {
        'detail': detail
    }
    
    return render(request, "single-product.html", context=context)

def home(request):
    products = ProductDetail.objects.all()
    blogs = SingleBlog.objects.all()
    context = {
        'products': products,
        'blogs': blogs
    }
    return render(request,"index.html", context=context)