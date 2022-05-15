from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserOTP
import random
from django.core.mail import send_mail
from django.conf import settings

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
        get_otp = request.POST.get('otp')
        
        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username = get_usr)

            if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
                usr.is_active = True
                usr.save()
                # Profile.objects.create(user=usr, username=usr.username, email= usr.email)
                messages.add_message(request, messages.SUCCESS, f'"{usr.username}" verified and registered successfully!')
                return redirect('sign-in')
            else:
                messages.add_message(request, messages.WARNING, 'Invalid OTP! Please check again. ')
                
                return render(request, 'accounts/signUp.html', {'otp':True, 'usr':usr})
        
        
        userdata = CreateUserForm(request.POST)
        username = request.POST.get('username')
        if userdata.is_valid():
            userdata.save()
            usr = User.objects.get(username = username)
            usr.is_active= False
            usr.save()

            usr_otp = random.randint(100000, 999999)
            db_otp = usr_otp
            UserOTP.objects.create(user=usr, otp=db_otp)
            mail_message = f"Hello {usr.username}, \nYour OTP is {usr_otp}.\n\nThank You!\nTeam e-News. "

            send_mail(
                "Welcome to e-News -  Verify Your Email",
                mail_message,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently= False
            )
            return render(request, 'accounts/signUp.html', {'otp':True, 'usr':usr})
        else:
            messages.add_message(request, messages.ERROR, 'Failed to register user!!')

    context = {'form': CreateUserForm}

    return render(request, 'accounts/signUp.html', context)


def home(request):
    return render(request, 'accounts/home.html')
