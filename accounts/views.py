from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.

def signIn(request):
    return render(request, 'accounts/signIn.html')

def signUp(request):
    if request.method == 'POST':
        userdata = CreateUserForm(request.POST)
        username = request.POST.get('username')
        if userdata.is_valid():
            userdata.save()
            messages.add_message(request, messages.SUCCESS, f'"{username}" registered successfully!!')
        else:
            messages.add_message(request, messages.ERROR, 'Failed to register user!!')    
            
    context = {'form':CreateUserForm}
    
    return render(request, 'accounts/signUp.html', context)

def home(request):
    return render(request, 'accounts/home.html')
    
