from django.contrib import admin
from django.urls import path
from . import views

app_name = "myapp" #naming the app for namespace, so that it can be referenced in the template
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.products, name='products'),
    #path('products/', views.ProductListView.as_view(), name='products'),
    #path('products/<int:id>', views.product_detail, name =  'product_detail'), #the name parameter is to name the url for use in the template
    path('products/<int:pk>', views.ProductDetailView.as_view(), name = 'product_detail'),
    #path('products/add', views.add_products, name='add_products'),
    path('products/add', views.ProductCreateView.as_view(), name='add_products'),
    path('products/update/<int:id>/', views.update_product, name="update_product"),
    path('products/delete/<int:id>/', views.delete_product, name="delete_product"),
    path('products/mylistings', views.my_listings, name='mylistings'),
    path('success/',views.PaymentSuccessView.as_view(), name='success'),
    path('failed/', views.PaymentFailedView.as_view(), name = 'failed'),
    path('api/checkout-session/<id>', views.create_checkout_session, name='api_checkout_session'),
    
]


