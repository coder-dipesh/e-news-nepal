from django.urls import include, path
from editors import views

urlpatterns = [
    path('', views.editorDashboard, name='editor'),

    path('profile', views.editorProfile, name='profile'),

    # NEWS CRUD
    path('view-news', views.viewNews, name='view-news'),
    path('add-news', views.addNews, name='add-news'),
    path('update-news', views.updateNews, name='update-news'),





]
