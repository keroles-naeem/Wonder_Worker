from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('products/',views.products,name='products'),
    path('product/',views.product,name='product'),
    path('add_user/',views.user_page,name='user_page'),
    path('users/',views.users,name='users'),
    path('order/',views.create_order,name='order'),
    path('billing/',views.billing,name='billing'),
    path('add_to_bill/',views.add_to_bill,name='add_to_bill'),
    path('billing/<int:order_id>/product/<int:product_id>/remove/', views.remove_product, name='remove_product'),
    path('billing/<int:order_id>/product/<int:product_id>/quantity/<int:operation>/', views.quantity_controller, name='quantity_controller'),
    path('billing/product/', views.update_products, name='update_products'),

    
    # Add the remaining URL path configurations here
]