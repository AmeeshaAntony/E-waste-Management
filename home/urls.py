
from django.urls import path
from .views import home
from home import views
from .views import cart

urlpatterns = [
    path('home/', home, name='home'),
    path('overview/', views.overview, name='overview'),
    path('login/about.html', views.about, name='about'),
    path('login/causes.html', views.causes, name='causes'),
    path('login/effect.html', views.effect, name='effect'),
    path('login/solutions.html', views.solutions, name='solutions'),
    path('login/product_list.html', views.product, name='product'),
    path('login/order_track.html', views.order_track, name='order_track'),
    path('login/order.html', views.order, name='order'),
    path('login/contact.html', views.contact, name='contact'),
    path('login/overview.html', views.overview, name='overview'), 
    path('home/product_list.html', views.product, name='product'),
    path('home/help.html', views.help, name='help'),
    path('home/product_details.html', views.product_detail, name='product_detail'),
    path('home/order.html', views.order, name='order'),
    path('home/submit.html', views.submit, name='submit'),
    path('home/cart.html', views.cart, name='cart'),
    path('home/classify.html', views.classify, name='classify'),
    path('login/classify', views.classify, name='classify'),
    path('home/query.html', views.query, name='query'),
    path('home/about.html', views.about, name='about'),
    path('home/order_track.html', views.order_track, name='order_track'),

]
