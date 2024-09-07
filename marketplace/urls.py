from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('farmer_dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('buyer_dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('register/farmer/',views.register_farmer, name = 'register_farmer'),
    path('register/buyer/', views.register_buyer, name='register_buyer'),
    path('products/', views.product_list, name='product_list'),
    path('send_request/<int:product_id>/', views.send_request, name='send_request'),
    path('farmer_orders/', views.farmer_orders, name='farmer_orders'),
    path('order-summary/', views.order_summary, name='order_summary'),
    path('analis/', views.analis, name='analis'),
    path('profilemain/', views.profilemain, name='profilemain'),
    
       
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

