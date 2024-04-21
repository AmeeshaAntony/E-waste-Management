from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
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

def order_track(request):
    return render(request, 'order_track.html')

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

def classify(request):
    return render(request, 'classify.html')

def query(request):
    return render(request, 'query.html')

def cart(request):
    if request.method == 'POST':
        product_id_str = request.POST.get('product_id')
        if product_id_str:  # Check if 'product_id' is not empty
            try:
                product_id = int(product_id_str)
                product = get_object_or_404(Product, pk=product_id)
            # Further processing
                return redirect('cart')  # Redirect to the cart page or any other appropriate page
            except ValueError:
            # Handle the case when 'product_id' is not a valid integer
                return render(request, 'home.html', {'message': 'Invalid product ID'})
        else:
        # Handle the case when 'product_id' is not provided in the request
            return render(request, 'about.html', {'message': 'Product ID is missing'})
    else:
    # Handle other HTTP methods (e.g., GET)
    # Render the cart page
        return render(request, 'cart.html')

def process_classification(request):
    if request.method == 'POST':
        classification = request.POST.get('classification')
        if classification == 'plastic':
            # Perform actions for plastic classification
            return HttpResponse('E-Waste classified as plastic.')
        elif classification == 'metal':
            # Perform actions for metal classification
            return HttpResponse('E-Waste classified as metal.')
        else:
            return HttpResponse('Invalid classification.')
    else:
        return HttpResponse('Method not allowed.')
