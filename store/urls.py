from django.urls import path
from .views import ProductList
urlpatterns = [
    path('', ProductList, name='product_list'),
]
