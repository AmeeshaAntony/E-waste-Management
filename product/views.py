from django.shortcuts import render, get_object_or_404
from .models import Product

# View to display all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# View to display details of a specific product
def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


