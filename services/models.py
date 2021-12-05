from django.db import models
from django.db.models.fields import CharField, DateField
from django.db.models.fields.files import ImageField

# Create your models here.
class Service(models.Model):
    title=models.CharField(max_length=20)
    content=models.CharField(max_length=50)
    image=models.ImageField(upload_to='servicies')
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta:
        verbose_name='service'
        verbose_name_plural='services'

    def __str__(self):
        return(self.title)
        
