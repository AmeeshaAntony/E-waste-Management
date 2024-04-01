from django.shortcuts import render, redirect
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemForm

def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            return redirect('order_detail', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'order/create_order.html', {'form': form})

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'order/order_detail.html', {'order': order, 'order_items': order_items})
