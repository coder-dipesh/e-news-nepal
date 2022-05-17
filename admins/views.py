from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
from django.contrib.auth.models import User



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