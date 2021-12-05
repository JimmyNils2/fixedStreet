from django.contrib import admin
from .models import Service

# Register your models here.

class ServicieAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(Service,ServicieAdmin)