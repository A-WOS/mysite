from django.urls import path
from . import views

app_name = 'product'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
    # path('/register', views.register, name='register'),
    path('create/', views.ProductCreate.as_view(), name='register'),
    path('product/delete/<int:product_id>/', views.product_delete, name='product_delete'),

]
