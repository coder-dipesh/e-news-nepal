from django.urls import include, path
from editors import views

urlpatterns = [
    path('', views.editorDashboard, name='editor'),


]