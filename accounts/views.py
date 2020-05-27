from django.shortcuts import render, redirect
from .models import *
from .form import OrderForm, CreateUserForm, CustomerForm
from django.forms import inlineformset_factory
from .filters import OrderFilter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import orginal_function, allowed_user
from django.contrib.auth.models import Group


# Create your views here.
@login_required(login_url='login')
@allowed_user(allowed_roles='admin')
def homepage(request):
    order = Orders.objects.all()
    customers = Customer.objects.all()
    total_order = order.count()
    order_delivered = order.filter(status='DIR').count()
    order_pending = order.filter(status='PEN').count()

    context = {
        'order': order,
        'customer': customers,
        'order_delivered': order_delivered,
        'order_pending': order_pending,
        'total_order': total_order,

    }
    return render(request, 'accounts/dashboard.html', context)


@allowed_user(allowed_roles='admin')
def product(request):
    products = Product.objects.all()
    context = {
        'product': products
    }
    return render(request, 'accounts/Product.html', context)


@login_required(login_url='login')
def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    order = customers.orders_set.all()
    f = OrderFilter(request.GET, queryset=order)
    order = f.qs
    context = {
        'cust': customers,
        'order': order,
        'filter': f
    }
    return render(request, 'accounts/Customer.html', context)


def create_order(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Orders, fields=('product', 'status'))
    customer = Customer.objects.get(id=pk)
    formSet = OrderFormSet(instance=customer)
    if request.method == 'POST':
        formSet = OrderFormSet(request.POST, instance=customer)
        if formSet.is_valid():
            formSet.save()
            return redirect('homePage')

    context = {
        'fromSet': formSet
    }
    return render(request, 'accounts/create.html', context)


def update_order(request, pk):
    orders = Orders.objects.get(id=pk)
    form = OrderForm(instance=orders)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=orders)
        if form.is_valid():
            form.save()
            return redirect('homePage')
    context = {
        'form': form
    }

    return render(request, 'accounts/update.html', context)


@allowed_user(allowed_roles='admin')
def delete_order(request, pk):
    order = Orders.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('homePage')
    context = {
        'order': order
    }

    return render(request, 'accounts/delete.html', context)


@orginal_function
def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            group = ''
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group == 'customer':
                return redirect('user_page')
            elif group == 'admin':
                return redirect('homePage')
    return render(request, 'accounts/login.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


def logOut(request):
    logout(request)
    return redirect('homePage')


def user_dashboard(request):
    users = request.user.customer.orders_set.all()
    context = {
        'order': users,
        'total_order': users.count()

    }
    return render(request, 'accounts/user_dashboard.html', context)


def user_profile(request):
    cus = request.user.customer
    form = CustomerForm(instance=cus)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=cus)
        if form.is_valid():
            form.save()
            return redirect('user_page')
    context = {
        'form': form
    }
    return render(request, 'accounts/user_account.html', context)
