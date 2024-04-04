from django.shortcuts import get_object_or_404

from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Cart,Product


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

def submit(request):
    return render(request, 'submit.html')

def cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        try:
            product_id = int(product_id)
            print(product_id)
        except ValueError:
            return render(request, 'order.html', {'message': 'Invalid product ID'})
        
        try:
            product = get_object_or_404(Product, pk=product_id)
        except Product.DoesNotExist:
            return render(request, 'home.html', {'message': 'Product does not exist'})

        # Continue with your view logic
        # ...
    else:
        cart_obj = Cart.objects.all()  # Retrieve cart items from the database
    
    context = {'cart': cart_obj}
    
    return render(request, 'cart.html', context)
