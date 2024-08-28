from django.db import models
from django.contrib.auth import get_user_model
from decimal import Decimal
from django.utils import timezone
from django.db.models import Avg
from django.shortcuts import render
# Create your models here.
User = get_user_model()

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BlogComment(TimeStamp):
    blog = models.ForeignKey("SingleBlog", on_delete=models.CASCADE, related_name="blogcomment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    body = models.TextField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="blog_parent", null=True, blank=True)
    rating = models.IntegerField()


class SingleBlog(TimeStamp):
    image = models.ImageField(upload_to="singleblog_img")
    title = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "userblog")
    note = models.TextField()
    description = models.TextField()
    category = models.ForeignKey("Category", on_delete= models.CASCADE, related_name="category_blog")
    description2 = models.TextField()
    
      
class Discount(models.Model):
    rate = models.IntegerField()

    
class Like(models.Model):
    blog = models.ForeignKey(SingleBlog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
class Color(models.Model):
    name = models.CharField(max_length=50)
    hex_value = models.CharField(max_length=7)
    def __str__(self) -> str:
        return self.name
    
    
class Size(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
    
class ImageProduct(models.Model):
    image = models.ImageField(upload_to="product_img")
    product = models.ForeignKey("ProductDetail", on_delete=models.CASCADE, related_name= "product_image")
    is_primary = models.BooleanField(default=False)
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image_product")
    bestbrend = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    
    
class ProductDetail(models.Model):
    description = models.TextField()
    product =models.ForeignKey(Product, on_delete=models.CASCADE ,related_name= "product")
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    gty = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey("ProductCategory", on_delete=models.CASCADE)
    shipping = models.DecimalField(max_digits=10, decimal_places=2)
    brend = models.ForeignKey("Brand", on_delete= models.CASCADE, related_name= "brand",null= True, blank=True)
    tag = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def discounted_price(self):
        if self.discount:
            discount_rate = Decimal(self.discount.rate) / Decimal(100)
            return round(self.price * (1 - discount_rate),2)
        return self.price
    
    def __str__(self) -> str:
        return self.product.name
    
    def average_rating(self):
        ratings = Rating.objects.filter(product=self)
        if ratings.exists():
            return ratings.aggregate(models.Avg('score'))['score__avg']
        return 0

    def full_star_count(self):
        return int(self.average_rating())

    def empty_star_count(self):
        return 5 - (self.full_star_count() + self.half_star_count())
    
    def rating_count(self):
        return Rating.objects.filter(product=self).count()
    
class Category(models.Model):
    name = models.CharField( max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="sub_categorys", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name 
    
    
class Brand(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
    
class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="sub_categorys", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.name
    
    
class Rating(models.Model):
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Reytinq balı (1-dən 5-ə qədər)
    comment = models.TextField(blank=True, null=True)  # İstəyə bağlı şərh

    class Meta:
        unique_together = ('user', 'product') 

    

def get_product_rating(product):
    ratings = Rating.objects.filter(product=product)
    if ratings.exists():
        return ratings.aggregate(Avg('score'))['score__avg'] or 0
    return 0

def product_list(request):
    products = ProductDetail.objects.all()
    product_ratings = {product.pk: get_product_rating(product.pk) for product in products}
    star_range = range(1, 6)  # 1-dən 5-ə qədər olan ulduzlar
    return render(request, "product-list.html", {"products": products, "product_ratings": product_ratings, "star_range": star_range})


def average_rating(self):
    ratings = Rating.objects.filter(product=self)
    if ratings.exists():
        avg_rating = ratings.aggregate(models.Avg('score'))['score__avg']
        return round(avg_rating, 1)  # Rəqəmsal dəyəri 1 onluq yerinə yuvarlaqlaşdırın
    return 0

def rating_count(self):
    return Rating.objects.filter(product=self).count()
