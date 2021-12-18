from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path('', views.default),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register_view),
    path('logout/', views.logout_view),
    path('sale/', views.sale_view),
    path('new/', views.new_view),
    path('home/', views.home_view),
    path('chat/', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('contact/', views.contact_view),



   # path('chat/<str:room_name>/<str:userName>/', views.room, name='room')


]