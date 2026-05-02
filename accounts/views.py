import json
import time
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import * # from .forms import OrderForm  <-- Uncomment this later when you add forms

# --- NEW IMPORTS FOR THE ATTACK PROJECT ---
import pickle
import base64
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# ------------------------------------------

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

# --- VULNERABLE ENDPOINT FOR ASSIGNMENT ---
@csrf_exempt
def vulnerable_import(request):
    """
    SECURED VIEW: 
    This endpoint now uses JSON instead of Pickle. 
    JSON only parses static data structures and cannot execute arbitrary code.
    """
    if request.method == 'POST':
        try:
            # THE BRICK WALL: We now expect JSON.
            # If the attacker sends a base64 pickle payload, this line will fail and crash safely.
            preferences = json.loads(request.body)
            
            return JsonResponse({"status": "success", "message": "Data securely imported."})
        
        except json.JSONDecodeError:
            # The payload is caught and rejected here, BEFORE any code can be executed.
            return JsonResponse({"status": "error", "message": "Invalid JSON format. Potential attack blocked."}, status=400)
            
    return JsonResponse({"status": "error", "message": "Only POST requests allowed."}, status=405)

@csrf_exempt
def legacy_import_honeypot(request):
    """
    DECEPTION VIEW: 
    This looks like an old, forgotten, vulnerable API endpoint. 
    It intentionally wastes the attacker's time and returns a fake success message.
    """
    if request.method == 'POST':
        # Tarpitting: Pause the server for 5 seconds to slow down automated hacking tools
        time.sleep(5)
        
        # Deception: Throw the data in the trash, but tell the attacker it worked
        return JsonResponse({"status": "success", "message": "Legacy preferences loaded."})
        
    return JsonResponse({"status": "error", "message": "Only POST allowed"}, status=405)