from accounts import views
from django.urls import  path

urlpatterns = [
  
  # Login Register
  path('sign-in', views.signIn, name='sign-in'),
  path('sign-up', views.signUp, name='sign-up'),
  
  
  
  path('', views.home, name='home'),
  
  
]