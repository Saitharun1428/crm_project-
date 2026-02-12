from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * # from .forms import OrderForm  <-- Uncomment this later when you add forms

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending
    }

    return render(request, 'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'accounts/customer.html', context)

# --- NEW FUNCTIONS ADDED BELOW TO FIX THE ERROR ---

def createCustomer(request):
    # Placeholder: Just renders the dashboard for now to prevent crashing
    # Later you will add: return render(request, 'accounts/customer_form.html', context)
    return redirect('home')

def createOrder(request, pk):
    # Placeholder
    return redirect('home')

def updateOrder(request, pk):
    # Placeholder
    return redirect('home')

def deleteOrder(request, pk):
    # Placeholder
    return redirect('home')