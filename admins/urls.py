from django.urls import include, path
from admins import views

urlpatterns = [
  path('', views.adminDashbaord, name='admins'),
  
  path('all-users', views.getUsers, name='all-users'),
  
  
  
  
  
  path('all-editors', views.getEditor, name='all-editors'),
  path('editor-sign-up', views.editorSignUp, name='editor-sign-up'),



]