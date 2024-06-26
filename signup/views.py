# views.py

from django.shortcuts import render, redirect
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the home page after successful signup
            return redirect('home')  # Replace 'home' with the name of your home page URL pattern
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# Create your views here.
