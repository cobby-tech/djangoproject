from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from .models import ThriftItem
from .forms import ThriftItemForm

def home(request):
    return render(request, 'home.html')

def products(request):
    query = request.GET.get('q')
    if query:
        items = ThriftItem.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        items = ThriftItem.objects.all()
    return render(request, 'products.html', {'items': items, 'query': query})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ThriftItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return redirect('products')
    else:
        form = ThriftItemForm()
    return render(request, 'add_product.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')