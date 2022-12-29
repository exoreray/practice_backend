# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("valid")
            # Save the user's form data to the database
            user = form.save()
            # Hash the password
            user.set_password(user.password)
            user.save()
            # Send an email to the user to confirm their registration
            # Redirect the user to the login page
            return redirect('login')
        print("not alid")
    
    else:
        print("here")
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect the user to the home page
            return redirect('home')
        else:
            # Render the login page with an error message
            return render(request, 'registration/login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'registration/login.html')

def home(request):
    return render(request, 'home.html')