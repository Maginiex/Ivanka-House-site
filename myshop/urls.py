from django.urls import path
from . import views
from cart import views as v

app_name = 'myshop'

urlpatterns = [
     path('', views.product_list, name='product_list'),
     path('<slug:category_slug>/', views.product_list,
          name='product_list_by_category'
          ),
     path('<int:id>/<slug:slug>', views.product_detail,
          name='product_detail'),
     path('<int:id>/cart', views.product_detail,
          name='product_detail'),
     path("cart",v.cart_detail, name='cart_detail'), 
     path("orders/cart",v.cart_detail, name='cart_detail'), 
     ]