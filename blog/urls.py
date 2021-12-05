from . import views
from django.urls import path

urlpatterns = [

    path('', views.blog, name='blog'),
    path('category/<category_id>',views.category, name='category'),
    
]