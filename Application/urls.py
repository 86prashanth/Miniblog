from django.urls import path
from .views import * 

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('dashboard/',dashboard,name='dashboard'),
    path('logout/',user_logout,name='logout'),
    path('signup/',user_signup,name='signup'),
    path('login/',user_login,name='login'),
    path('addpost/',add_post,name='addpost'),
    path('updatepost/<int:id>/',update_post,name='updatepost'),
    path('deletepost/<int:id>/',delete_post,name='deletepost'),
]
