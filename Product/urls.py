from django.urls import path
from .views import *

app_name = 'Product'

urlpatterns = [
    path('all/', all_products, name='all'),
    path('delete/<int:id>/', product_delete, name='delete'),
]