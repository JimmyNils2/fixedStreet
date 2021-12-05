from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def __str__(self):
        return(self.name)
        
class Post(models.Model):
    title=models.CharField(max_length=20)
    content=models.CharField(max_length=50)
    image=models.ImageField(upload_to='blog', null=True, blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return(self.title)
        