from django.db import models
from django.contrib.auth import get_user_model

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


class SingleBlog(TimeStamp):
    image = models.ImageField(upload_to="singleblog_img")
    title = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= "userblog")
    note = models.TextField()
    description = models.TextField()
    blog = models.ForeignKey("Blog", on_delete= models.CASCADE , related_name= "blog")
    category = models.ForeignKey("Category", on_delete= models.CASCADE, related_name="category_blog")
    brend = models.ForeignKey("Brand", on_delete= models.CASCADE, related_name= "blog_brand")
    
     

        
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="singleblog_img")
    
    
class Discount(models.Model):
    rate = models.IntegerField()
    
    
class Like(models.Model):
    blog = models.ForeignKey(SingleBlog, on_delete=models.CASCADE)
    
    
class Color(models.Model):
    name = models.CharField(max_length=50)
    
    
class Size(models.Model):
    name = models.CharField(max_length=50)
    
    
class ImageProduct(models.Model):
    image = models.ImageField(upload_to="product_img")
    product = models.ForeignKey("ProductDetail", on_delete=models.CASCADE)
    
class Rating(models.Model):
    value = models.IntegerField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="image_product")
    
class ProductDetail(models.Model):
    description = models.TextField()
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    gty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey("ProductCategory", on_delete=models.CASCADE)
    
class Category(models.Model):
    name = models.CharField( max_length=100)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="categorys", null=True, blank=True)
    
class Brand(models.Model):
    name = models.CharField(max_length=50)
    
class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="sub_categorys", null=True, blank=True)
    