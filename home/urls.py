
from django.urls import path
from .views import home
from home import views

urlpatterns = [
    path('home/', home, name='home'),
    path('overview/', views.overview, name='overview'),
    path('home/about.html', views.about, name='about'),
    path('home/causes.html', views.causes, name='causes'),
    path('home/effect.html', views.effect, name='effect'),
    path('home/solutions.html', views.solutions, name='solutions'),
    path('home/product_list.html', views.product, name='product'),
]
