from django.shortcuts import render, get_object_or_404, redirect
from .models import  ProductDetail, Product,SingleBlog,ProductCategory, Category,Brand,Size,Color,ImageProduct, get_product_rating,rating_count,Rating
from orders.models import Wishlist
from django.http import JsonResponse
from django.db import models
# Create your views here.
def blog(request):
    blogs = SingleBlog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, "blog.html", context=context)

def product_list(request):
    products = ProductDetail.objects.all()
    bestbrend = Product.objects.first()
    all_brend = Brand.objects.all()
    product_ratings_count = {
        product.pk: Rating.objects.filter(product=product).count() for product in products
    }

    product_ratings = {product.pk: get_product_rating(product) for product in products}
    qrup = len(all_brend)// 2
    group1_brands = all_brend[:qrup]
    group2_brands = all_brend[qrup:]
    sizes = Size.objects.all()
    context = {
        'group1_brands': group1_brands,
        'group2_brands': group2_brands,
        'bestbrend': bestbrend,
        'sizes': sizes,
        'products': products,
        'product_ratings': product_ratings,
        'star_range': range(1, 6),
        'product_ratings_count': product_ratings_count,

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
    rating = detail.average_rating()
    star_range = range(1, 6)
    rating_count = detail.rating_count()
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
        'quantity': quantity,
        'error_message': error_message,
        'rating': rating,
        'star_range': star_range,
        'rating_count': rating_count,
    }
    
    return render(request, "single-product.html", context=context)

def home(request):
    products = ProductDetail.objects.all()
    blogs = SingleBlog.objects.all()
    # new_collection = Product.objects.filter(new_collection = True)
    products_with_discount = ProductDetail.objects.filter(discount__isnull=False).order_by('-discount__rate')[:3]
    
    context = {
        'products': products,
        'blogs': blogs,
        # 'new_collection': new_collection,
        'products_with_discount': products_with_discount

    }
    return render(request,"index.html", context=context)

