from . import views
from django.urls import path

app_name='cart'

urlpatterns = [

    path('add/<int:product_id>/', views.add_product, name='add'),
    path('delete/<int:product_id>/', views.delete_product, name='delete'),
    path('subtract/<int:product_id>/', views.subtract_product, name='subtract'),
    path('empty/', views.empty_cart, name='empty'),
    
]