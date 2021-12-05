from django.db import models

# Create your models here.

class ProdCategory(models.Model):

    name=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='prodcategory'
        verbose_name_plural='prodcategories'

    def __str__(self):
        return (self.name)


class Product(models.Model):

    name=models.CharField(max_length=50)
    categories=models.ForeignKey(ProdCategory, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='store')
    price=models.FloatField()
    available=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='product'
        verbose_name_plural='products'