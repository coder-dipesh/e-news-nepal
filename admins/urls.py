from django.urls import include, path
from admins import views

urlpatterns = [
  path('', views.adminDashbaord, name='admins'),
  
  
  
  
]