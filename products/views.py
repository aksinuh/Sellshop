from django.shortcuts import render, get_object_or_404, redirect
from .models import  ProductDetail, Product,SingleBlog,ProductCategory, Category,Brand,Size,Color,ImageProduct
from orders.models import Wishlist
from django.http import JsonResponse
# Create your views here.
def blog(request):
    blogs = SingleBlog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, "blog.html", context=context)

def product_list(request):
    bestbrend = Product.objects.first()
    all_brend = Brand.objects.all()
    qrup = len(all_brend)// 2
    group1_brands = all_brend[:qrup]
    group2_brands = all_brend[qrup:]
    sizes = Size.objects.all()
    context = {
        'group1_brands': group1_brands,
        'group2_brands': group2_brands,
        'bestbrend': bestbrend,
        'sizes': sizes
    }
    
    return render(request, "product-list.html",context=context)

def single_blog(request, id):
    blog = SingleBlog.objects.get(id=id)
    latest_products = ProductDetail.objects.all().order_by('-created_at')[:3]
    categorys = Category.objects.filter(parent= None)
    all_brend = Brand.objects.all()
    qrup = len(all_brend)// 2
    group1_brands = all_brend[:qrup]
    group2_brands = all_brend[qrup:]
    bestbrend = Product.objects.first()
    context = {
        'blog': blog,
        'latest_products':latest_products,
        'categorys': categorys,
        'group1_brands': group1_brands,
        'group2_brands': group2_brands,
        'bestbrend': bestbrend
        
    }
    return render(request, "single-blog.html", context=context)


def single_product(request, id):
    detail = get_object_or_404(ProductDetail, id=id)
    bestbrend = ProductDetail.objects.get(product__id=id)
    max_quantity = detail.gty
    quantity = 1
    error_message = ''

    if request.method == 'POST':
        try:
            quantity = int(request.POST.get('qtybutton', 1))
            if quantity > max_quantity:
                error_message = 'Seçdiyiniz miqdar mövcud stokdan çoxdur!'
                quantity = max_quantity
            else:
                wishlist, created = Wishlist.objects.get_or_create(user=request.user)
                wishlist.product.add(detail)
                # Burada məhsulu və miqdarı wishlist-ə əlavə edə bilərsiniz
                return redirect('wishlist')
        except ValueError:
            error_message = 'Zəhmət olmasa düzgün bir miqdar daxil edin!'
    
    context = {
        'detail': detail,
        'bestbrend': bestbrend,
        'quantity': quantity,
        'error_message': error_message
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

