from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from datetime import datetime
class Image(models.Model):
    imagename = models.CharField(max_length=20)
    img = models.ImageField(upload_to= "images/")

    def __str__(self):
        return self.imagename





class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
   
class Shoes(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shoename = models.CharField(max_length=20)
    color = models.CharField(max_length=20, default='')
    size = models.CharField(max_length=50, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
    sex = models.CharField(max_length=10)
    upload = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.shoename


    
class JacketCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Jacket(models.Model):
    jacketname = models.ForeignKey(JacketCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default= '')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
    color = models.CharField(max_length=20, default='')
    size = models.CharField(max_length=50, default='')
    sex = models.CharField(max_length=10)
    upload = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class ShirtCategory(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Shirt(models.Model):

    shirtname = models.ForeignKey(ShirtCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default= '')
    color = models.CharField(max_length=50, default='')
    size = models.CharField(max_length=50, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
    sex = models.CharField(max_length=10)
    upload = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.name

class DummyUpload(models.Model):
    name = models.CharField(max_length=20)
    media = models.ImageField(upload_to='images/')

 
class Cart_Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    cart_product = GenericForeignKey('content_type', 'object_id')

    @property
    def total_price(self):
        return self.cart_product.price * self.quantity

    def __str__(self):
        return f'{self.quantity} x {self.cart_product}'
    
    
class Comment(models.Model):
    comment = models.CharField(max_length=200)

class logo(models.Model):
    image = models.ImageField(upload_to='images/')

class ChatSpace(models.Model):
    space = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default = '')

    def __str__(self):
        return self.space
    
class Message(models.Model):
    space = models.ForeignKey(ChatSpace, on_delete=models.CASCADE)
    user = models.CharField(max_length=250)
    message = models.TextField(max_length=250 , default = 'null')
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'{self.space} X {self.user}'


class location(models.Model):
    location = models.CharField(max_length=20)
