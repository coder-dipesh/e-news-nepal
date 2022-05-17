from django.urls import include, path
from admins import views

urlpatterns = [
  path('', views.adminDashbaord, name='admins'),
  path('admin_editor', views.admin_editor, name='admin_editor'),
  path('editor_signUp', views.editor_signUp, name='editor_signUp'),



]