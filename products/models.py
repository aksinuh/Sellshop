from django.db import models
from django.contrib.auth import get_user_model
from decimal import Decimal
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
    
    def __str__(self) -> str:
        return self.name
    
    
class Size(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    
    
class ImageProduct(models.Model):
    image = models.ImageField(upload_to="product_img")
    product = models.ForeignKey("ProductDetail", on_delete=models.CASCADE)
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image_product")
    
    def __str__(self) -> str:
        return self.name
    
    
class ProductDetail(models.Model):
    description = models.TextField()
    product =models.ForeignKey(Product, on_delete=models.CASCADE ,related_name= "product")
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    gty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey("ProductCategory", on_delete=models.CASCADE)
    shipping = models.DecimalField(max_digits=10, decimal_places=2)
    brend = models.ForeignKey("Brand", on_delete= models.CASCADE, related_name= "brand",null= True, blank=True)
    tag = models.BooleanField(default=True)
    
    def discounted_price(self):
        if self.discount:
            discount_rate = Decimal(self.discount.rate) / Decimal(100)
            return round(self.price * (1 - discount_rate),2)
        return self.price
    
    
class Category(models.Model):
    name = models.CharField( max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="categorys", null=True, blank=True)
    
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