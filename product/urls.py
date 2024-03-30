from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('product/', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]
