from accounts import views
from django.urls import  path,include

urlpatterns = [
  # Socail Auth 
  path('',include('django.contrib.auth.urls')),

  
  # Login Register
  path('sign-in', views.signIn, name='sign-in'),
  path('sign-up', views.signUp, name='sign-up'),
  path('sign-out', views.signOut, name='sign-out'),
  
  path('', views.home, name='home'),
  
  
]