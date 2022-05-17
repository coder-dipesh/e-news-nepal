from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
from django.contrib.auth.models import User

from accounts.auth import admin_only, unauthenticated_user

# Create your views here.
from accounts.forms import CreateUserForm
from enews import settings


@login_required
@admin_only
def adminDashbaord(request):
    users = User.objects.all()
    
    admin_count = users.filter(is_superuser=1).count()
    editor_count = users.filter(is_superuser=0,is_staff=1).count()
    user_count = users.filter(is_superuser=0,is_staff=0).count()
    
    user_info= users.exclude(is_superuser=1)
    
    
    context = {'users': users,
                'admin_count': admin_count,
                'editor_count': editor_count,
                'user_count': user_count,
                'user_info': user_info,
                
                }
    return render(request, 'admins/adminDashboard.html',context)

@login_required
@admin_only
def getUsers(request):
    users = User.objects.all()
    user_info = users.filter(is_superuser=0,is_staff=0)
    context = {'user_info': user_info,
                'activate_users':'active'}
    
    return render(request, 'admins/allUsers.html',context)
    return render(request, 'admins/adminDashboard.html')


@login_required
@admin_only
def admin_editor(request):
    return render(request, 'admins/adminEditor/editorPage.html')


@login_required
def editor_signUp(request):
    if request.method == 'POST':
        get_otp = request.POST.get('otp')

        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)

        userdata = CreateUserForm(request.POST)
        username = request.POST.get('username')
        if userdata.is_valid():
            userdata.save()
            usr = User.objects.get(username=username)
            usr.is_active = False
            usr.save()

            mail_message = f"Hello {usr.username}, \n You are Registered as e-News Nepal Editor \n\nThank You!\nTeam " \
                           f"e-News. "

            send_mail(
                "Welcome to e-News Nepal",
                mail_message,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )
            return render(request, 'admins/adminEditor/registerEditor.html', {'usr': usr})
        else:
            messages.add_message(request, messages.ERROR, 'Failed to register user!!')

    context = {'form': CreateUserForm}

    return render(request, 'admins/adminEditor/registerEditor.html', context)
