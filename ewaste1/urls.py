from django.urls import path
from . import views

urlpatterns = [
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/signup.html', views.signup, name='signup'),
    path('login/login2.html', views.login, name='login2'),
    path('login/login2.html/home.html', views.logined, name='logined'),
]
