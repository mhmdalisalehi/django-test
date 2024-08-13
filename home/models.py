from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category/', blank=True)
    slug = models.SlugField(max_length=100, unique=True,null=True,blank=True)
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    is_subcategory = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category', args=[self.slug, self.id])


class Product(models.Model):
    VARIANT=(
        ('None','none'),
        ('Color','color'),
        ('Size','size'),
    )
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product/')
    category = models.ManyToManyField(Category,)
    amount = models.IntegerField()
    unitPrice = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    discount = models.PositiveBigIntegerField()
    totalPrice = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100, unique=True,null=True,blank=True)
    status = models.CharField(max_length=200, choices=VARIANT, default='None',null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:details', args=[self.slug, self.id])

    @property
    def totalPrice(self):
        if not self.discount:
            return self.unitPrice
        elif self.discount:
            total = (self.discount * self.unitPrice)/100
            return int(self.unitPrice - total)
        return self.totalPrice


class Size(models.Model):
    name = models.CharField(max_length=100)

class Color(models.Model):
    name = models.CharField(max_length=100)

class Variants(models.Model):
    name = models.CharField(max_length=100)
    product_variant = models.ForeignKey(Product,on_delete=models.CASCADE)
    color_variant = models.ForeignKey(Color,on_delete=models.CASCADE)
    size_variant = models.ForeignKey(Size,on_delete=models.CASCADE)
    amount = models.IntegerField()
    unitPrice = models.PositiveIntegerField()
    discount = models.PositiveBigIntegerField()
    totalPrice = models.PositiveIntegerField()
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:details', args=[self.slug, self.id])

    @property
    def totalPrice(self):
        if not self.discount:
            return self.unitPrice
        elif self.discount:
            total = (self.discount * self.unitPrice)/100
            return int(self.unitPrice - total)
        return self.totalPrice


