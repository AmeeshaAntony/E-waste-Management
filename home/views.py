

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




