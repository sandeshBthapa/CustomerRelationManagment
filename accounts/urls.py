from django.urls import path
from .views import homepage, product, customer, create_order, update_order, delete_order, logins, register, logOut, \
    user_dashboard, user_profile

urlpatterns = [
    path('', homepage, name='homePage'),
    path('product/', product, name='product'),
    path('user_acc/', user_profile, name='user_acc'),
    path('user_page', user_dashboard, name='user_page'),
    path('customer/<str:pk>/', customer, name='customer'),
    path('createOrder/<str:pk>', create_order, name='create_order'),
    path('update_order/<str:pk>', update_order, name='update_order'),
    path('delete_order/<str:pk>', delete_order, name='delete_order'),
    path('login/', logins, name='login'),
    path('logout/', logOut, name='logout'),
    path('register/', register, name='register'),

]
