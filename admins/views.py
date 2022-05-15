from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
# Create your views here.

@login_required
@admin_only
def adminDashbaord(request):
    return render(request, 'admins/adminDashboard.html')