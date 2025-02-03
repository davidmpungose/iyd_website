from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .form import TenantRegistrationForm

def register_user(request):
    if request.method == 'POST':
        form = TenantRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account created. Please log in.')
            return redirect('login')
        else:
            messages.warning(request, 'Sorry. Something went wrong.')
            print(form.errors)
            context = {'form': form}
            return render(request, 'registration/register.html', context)
    else:
        form = TenantRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username = username, password = password)

        if user is not None and user.is_active:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Sorry. Something went wrong.')
            return redirect('login')
    else:
        return render(request, 'registration/login.html')
    
def logout_user(request):
    logout(request)
    return redirect('login')