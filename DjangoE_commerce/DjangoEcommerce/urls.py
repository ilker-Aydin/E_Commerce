
from django.urls import path
from . import views
app_name='DjangoEcommerce'
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.mainpage, name="mainpage" ),
    path('signup/',views.SignUpView.as_view(),name="signup"),
    path('register/',views.register,name="register"),
    path('addproduct/',views.add_product,name="addproduct"),
    path('products/',views.listproducts,name="products"),
    path('deleteproduct/<int:id>',views.DeleteProduct,name='DeleteProduct'),
    path('product_details/<int:product_id>/', views.product_details, name='product_details'),
    path('orderform/', views.orderform, name='orderform'),
    path('cart/', views.cart, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
]
