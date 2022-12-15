from django.db import models
from django.shortcuts import reverse
# Create your models here.
class Categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    class Meta:
        ordering=('name',)
    def get_url(self):
        return reverse('homee',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)

class Products(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(Categ,on_delete=models.CASCADE)
    def get_url(self):
        return reverse('details',args=[self.category.slug,self.slug])

class CartList(models.Model):
    cart_id=models.CharField(max_length=200,unique=True)
    date=models.DateTimeField(auto_now_add=True)
    def _str__(self):
        return self.cart_id

class CartItem(models.Model):
    prod=models.ForeignKey(Products,on_delete=models.CASCADE)
    cart=models.ForeignKey(CartList,on_delete=models.CASCADE)
    quan=models.IntegerField()
    active=models.BooleanField(default=True)
    def _str__(self):
        return self.prod
    def total(self):
        return self.prod.price * self.quan


