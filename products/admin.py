from django.contrib import admin
from .models import (
    BlogComment, SingleBlog,
    Product, ProductCategory, ProductDetail,
     Discount, Like, Color, Size, 
    ImageProduct,  Category, Brand
)

# Register your models here.



@admin.register(BlogComment)
class BlogCommentadmin(admin.ModelAdmin):
    list_display = ["id", "blog", "user", "body"]
    list_display_links = ["body"]
    

@admin.register(SingleBlog)
class SingleBlogadmin(admin.ModelAdmin):
    list_display = ["id", "title", "user", "description"]
    list_display_links = ["title"]
    
    
    
@admin.register(Discount)
class Discountadmin(admin.ModelAdmin):
    list_display = ["id", "rate"]
    list_display_links = ["rate"]
    

@admin.register(Like)
class Likeadmin(admin.ModelAdmin):
    list_display = ["id", "blog"]
    list_display_links = ["blog"]


@admin.register(Color)
class Coloradmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]


@admin.register(Size)
class Sizeadmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]
    
    
@admin.register(ImageProduct)
class ImageProductadmin(admin.ModelAdmin):
    list_display = ["id"]
    list_display_links = ["id"]
    

@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]
    
    
@admin.register(ProductDetail)
class ProductDetailadmin(admin.ModelAdmin):
    list_display = ["id", "product", "price", "description", "discount"]
    list_display_links = ["product"]
    
    
@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ["id", "name","parent"]
    list_display_links = ["name"]
    
    
@admin.register(Brand)
class Brandadmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]
    

@admin.register(ProductCategory)
class Brandadmin(admin.ModelAdmin):
    list_display = ["id", "name", "parent"]
    list_display_links = ["name"]

