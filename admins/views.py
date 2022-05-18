from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
from django.contrib.auth.models import User

from accounts.auth import admin_only, unauthenticated_user
from .models import CustomUser
# Create your views here.
from accounts.forms import CreateUserForm
from .forms import CustomUserForm, CreateUserForm
from enews import settings


@login_required
@admin_only
def adminDashbaord(request):
    users = User.objects.all()

    admin_count = users.filter(is_superuser=1).count()
    editor_count = users.filter(is_superuser=0, is_staff=1).count()
    user_count = users.filter(is_superuser=0, is_staff=0).count()

    user_info = users.exclude(is_superuser=1)

    context = {'users': users,
               'admin_count': admin_count,
               'editor_count': editor_count,
               'user_count': user_count,
               'user_info': user_info,

               }
    return render(request, 'admins/adminDashboard.html', context)


@login_required
@admin_only
def getUsers(request):
    users = User.objects.all()
    user_info = users.filter(is_superuser=0, is_staff=0)
    context = {'user_info': user_info,
               'activate_users': 'active'}

    return render(request, 'admins/allUsers.html', context)


@login_required
@admin_only
def getEditor(request):
    context = {'activate_editors': 'active'}
    return render(request, 'admins/adminEditor/editorPage.html', context)


@login_required
def editorSignUp(request):
    if request.method == 'POST':
        cform = CustomUserForm(request.POST)
        form = CreateUserForm(request.POST)
        role = request.POST.get('role')
        salary = request.POST.get('salary')
        if form.is_valid():
            user = form.save()
            user.save()
            # Getting user and altering its value
            username = request.POST.get('username')
            usr = User.objects.get(username=username)
            usr.is_staff = True
            usr.save()  # Save user

            if cform.is_valid():
                CustomUser.objects.create(user=user, role=role, salary=salary)
            messages.add_message(request, messages.SUCCESS,
                                 'Editor registered successfully!!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Unable to register editor!!')

    context = {'form': CreateUserForm,
               'cform': CustomUserForm, }

    return render(request, 'admins/adminEditor/registerEditor.html', context)


@login_required
@admin_only
def getCategory(request):
    context = {'activate_category': 'active'}
    return render(request, 'admins/Category/categoryPage.html', context)


@login_required
def newCategory(request):
    if request.method == 'POST':
        cform = CustomUserForm(request.POST)
        form = CreateUserForm(request.POST)
        role = request.POST.get('role')
        salary = request.POST.get('salary')
        if form.is_valid():
            user = form.save()
            user.save()
            # Getting user and altering its value
            username = request.POST.get('username')
            usr = User.objects.get(username=username)
            usr.is_staff = True
            usr.save()  # Save user

            if cform.is_valid():
                CustomUser.objects.create(user=user, role=role, salary=salary)
            messages.add_message(request, messages.SUCCESS,
                                 'Editor registered successfully!!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Unable to register editor!!')

    context = {'form': CreateUserForm,
               'cform': CustomUserForm, }

    return render(request, 'admins/Category/newCategory.html', context)
