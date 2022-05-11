from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .forms import CreateUserForm
from django.contrib import messages, auth


# Create your views here.

def signIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.is_superuser and user.is_staff and user.is_active:
                print("working")
                return redirect('/admins')
            elif not user.is_superuser and user.is_staff and user.is_active:
                return redirect('/editors')
            elif not user.is_superuser and not user.is_staff and user.is_active:
                return redirect('/users')
        else:
            print("working")
            messages.error(request, "Username or Password is incorrect.")
            return render(request, 'accounts/signIn.html', {})
    context = {}
    return render(request, 'accounts/signIn.html', context)


def signUp(request):
    if request.method == 'POST':
        userdata = CreateUserForm(request.POST)
        username = request.POST.get('username')
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, f'"{username}" registered successfully!!')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to register user!!')

    context = {'form': CreateUserForm}

    return render(request, 'accounts/signUp.html', context)


def home(request):
    return render(request, 'accounts/home.html')
