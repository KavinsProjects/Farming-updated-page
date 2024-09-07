from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from .models import *
# Create your views here.
from .forms import *

def home(request):
    return render(request, 'marketplace/home.html')

def about(request):
    return render(request, 'marketplace/about.html')

def products(request):
    return render(request, 'marketplace/products.html')

def services(request):
    return render(request, 'marketplace/services.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            
            user_type = request.POST.get('user_type')
            profile, created = Profile.objects.get_or_create(user=user)
            
            if not created:
                profile.user_type = user_type
                profile.save()
            
            messages.success(request,'Account was created for'+username)
            return redirect('login')
        else:
            messages.error(request, 'There was an error with your registration.')

    context={'form':form}
    return render(request,'marketplace/register.html',context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
           # return redirect('home')
            '''
            if user.profile.user_type == 'farmer':
                return redirect('farmer_dashboard')
            elif user.profile.user_type == 'buyer':
                return redirect('buyer_dashboard')
            '''
            try:
                profile = Profile.objects.get(user=user)
                if profile.user_type == 'farmer':
                    return redirect('farmer_dashboard')
                elif profile.user_type == 'buyer':
                    return redirect('buyer_dashboard')
            except Profile.DoesNotExist:
                messages.error(request, 'Profile does not exist for this user.')

        else:
            messages.info(request,'Username OR password is incorrect')

    context={}
    return render(request,'marketplace/login.html',context)

def farmer_dashboard(request):
    # Get the farmer's profile
    profile = get_object_or_404(Profile, user=request.user)

    # Ensure the profile user type is 'farmer'
    if profile.user_type != 'farmer':
        return render(request, 'marketplace/buyer_dashboard.html')  # or redirect to another page

    # Retrieve the Farmer instance using the User
    try:
        farmer = Farmer.objects.get(user=request.user)
    except Farmer.DoesNotExist:
        return render(request, 'marketplace/farmer_dashboard.html')  # or redirect to another page

    # Fetch the farmer's products
    products = Product.objects.filter(farmer=farmer)

    # Handle the form submission
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.farmer = farmer  # Set the farmer from the Farmer instance
            product.save()
    else:
        form = ProductForm()

    # Define any analytics data (this is a placeholder; you can customize it as needed)
    analytics_data = {
        'total_products': products.count(),
        'total_sales': 5000,  # Example: you can calculate based on actual sales data
        'revenue': 20000,  # Example: fetch revenue for the farmer
    }

    context = {
        'profile': profile,
        'products': products,
        'analytics_data': analytics_data,
        'form': form,
    }

    return render(request, 'marketplace/farmer_dashboard.html', context)

def buyer_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    products = Product.objects.filter(available=True)

    context = {
        'profile': profile,
        'products': products,
    }

    return render(request,'marketplace/buyer_dashboard.html')

def send_request(request, product_id):
    product = Product.objects.get(id=product_id)
    buyer = Buyer.objects.get(user=request.user)

    Request.objects.create(product=product, buyer=buyer)

    return redirect('buyer_dashboard')

def register_farmer(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            farmer = form.save(commit=False)
            farmer.user = request.user
            farmer.save()
            return redirect('login')

    else:
        form = FarmerRegistrationForm()
    return render(request, 'marketplace/register_farmer.html', {'form':form})

def register_buyer(request):
    if request.method == 'POST':
        form = BuyerRegistrationForm(request.POST)
        if form.is_valid():
            buyer = form.save(commit=False)
            buyer.user = request.user
            buyer.save()
            return redirect('login')

    else:
        form = BuyerRegistrationForm()
    return render(request, 'marketplace/register_buyer.html', {'form': form})

def product_list(request, product_id):
    products = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.buyer = request.user.buyer
            req.product = product
            req.save()
            return redirect('product_list')

    else:
        form = RequestForm()
    return render(request, 'send_request.html',{'form': form, 'product': product})

def send_request(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        # Create an Order instance (you need to create an Order model)
        Order.objects.create(
            product=product,
            buyer=request.user.profile,  # Assuming there's a Profile model linked to the user
            status='Pending'  # You might want to add more statuses like 'Accepted', 'Rejected', etc.
        )
        messages.success(request, 'Your order request has been sent.')
        return redirect('buyer_dashboard')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('buyer_dashboard')

def farmer_orders(request):
    orders = Order.objects.filter(product__farmer=request.user.profile)
    return render(request, 'marketplace/farmer_orders.html', {'orders': orders})

def order_summary(request):
    # Assuming you have an Order model linked to the user
    user_orders = Order.objects.filter(buyer=request.user)
    return render(request, 'marketplace/order_summary.html', {'orders': user_orders})

def analis(request):
    # Assuming you have an Order model linked to the use
    return render(request,'marketplace/analis',)

def profilemain(request):
    return render(request,'marketplace/profilemain.html')
