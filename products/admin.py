from django.contrib import admin
from .models import (
    TimeStamp, BlogComment, SingleBlog,
    Product, ProductCategory, ProductDetail,
    Blog, Discount, Like, Color, Size, 
    ImageProduct, Rating, Category, Brand
)
# Register your models here.

admin.site.register(TimeStamp)

@admin.register(BlogComment)
class BlogCommentadmin(admin.ModelAdmin):
    list_display = ["id", "blog", "user", "body"]
    list_display_links = ["body"]
    

@admin.register(SingleBlog)
class SingleBlogadmin(admin.ModelAdmin):
    list_display = ["id", "title", "user", "blog", "description"]
    list_display_links = ["title"]
    
@admin.register(Blog)
class Blogadmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]
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
    
@admin.register(Rating)
class Ratingadmin(admin.ModelAdmin):
    list_display = ["id", "value", "product"]
    list_display_links = ["value"]
    
@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    list_display_links = ["name"]
    
@admin.register(ProductDetail)
class ProductDetailadmin(admin.ModelAdmin):
    list_display = ["id", "discount", "price", "size", "color", "description", "product"]
    list_display_links = ["discount"]
    
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

