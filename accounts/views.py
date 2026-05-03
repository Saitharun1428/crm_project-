import pickle
import base64
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *

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

def createCustomer(request):
    return redirect('home')

def createOrder(request, pk):
    return redirect('home')

def updateOrder(request, pk):
    return redirect('home')

def deleteOrder(request, pk):
    return redirect('home')

# VULNERABLE ENDPOINT - uses pickle.loads() on untrusted data
@csrf_exempt
def vulnerable_import(request):
    if request.method == 'POST':
        data = base64.b64decode(request.body)
        preferences = pickle.loads(data)
        return JsonResponse({"status": "success", "message": "Preferences imported."})
    return JsonResponse({"status": "error", "message": "Only POST allowed."}, status=405)