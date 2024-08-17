from django.db import models
from accounts.models import User


# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey('accounts.User', related_name='data', on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Data, self).save(*args, **kwargs)
