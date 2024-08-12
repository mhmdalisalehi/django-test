from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category/')


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField()
    unitPrice = models.PositiveIntegerField()
    discount = models.PositiveBigIntegerField()
    totalPrice = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def totalPrice(self):
        if not self.discount:
            return self.unitPrice
        elif self.discount:
            total = (self.discount * self.unitPrice)/100
            return int(self.unitPrice - total)
        return self.totalPrice
