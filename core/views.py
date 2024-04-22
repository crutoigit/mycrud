from django.shortcuts import redirect, render
from item.models import Category, Item
from django.contrib.auth import logout

from .forms import SignUpForm

def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request,'core/index.html',{'items':items, 'categories':categories})

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignUpForm()
            
    return render(request,'core/signup.html', {'form':form})

# Logica de login este implementata by default in url-uri

def logout_user(request):
    logout(request) # insusi logout
    return redirect('/') # dupa ce iesim din cont ajungem la pagina principala
