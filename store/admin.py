from blog.admin import CategoryAdmin
from django.contrib import admin
from .models import ProdCategory,Product

# Register your models here.

class ProCategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')

class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')


admin.site.register(ProdCategory,ProCategoryAdmin)

admin.site.register(Product,ProductAdmin)