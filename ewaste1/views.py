

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            return render(request,'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


