from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, "blog.html")

def product_list(request):
    return render(request, "product-list.html")

def single_blog(request):
    return render(request, "single-blog.html")


def single_product(request):
    return render(request, "single-product.html")

def home(request):
    return render(request,"index.html")