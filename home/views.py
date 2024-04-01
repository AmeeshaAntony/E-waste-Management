

from django.shortcuts import render
from django.urls import reverse_lazy

def home(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, 'home.html', {'username': username})
    overview_url = reverse_lazy('overview')
    return render(request, 'home.html', {'overview_url': overview_url})


def overview(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def causes(request):
    return render(request, 'causes.html')

def effect(request):
    return render(request, 'effect.html')

def solutions(request):
    return render(request, 'solutions.html')

def product(request):
    return render(request, 'product_list.html')

def help(request):
    return render(request, 'help.html')

def product_detail(request):
    return render(request, 'product_detail.html')

def order(request):
    return render(request, 'order.html')

