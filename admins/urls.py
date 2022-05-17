from django.urls import include, path
from admins import views

urlpatterns = [
  path('', views.adminDashbaord, name='admins'),
  
  path('all-users', views.getUsers, name='all-users'),
  
  
  
  
  
]