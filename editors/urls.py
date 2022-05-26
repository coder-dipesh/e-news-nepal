from django.urls import include, path
from editors import views

urlpatterns = [
    path('', views.editorDashboard, name='editor'),

    path('profile', views.editorProfile, name='profile'),

    # NEWS CRUD
    path('my-news', views.myNews, name='my-news'),
    path('add-news', views.addNews, name='add-news'),
    path('update-news/<int:news_id>', views.updateNews, name='update-news'),
    path('delete-news/<int:news_id>', views.deleteNews, name='delete-news'),

    path('request_news', views.request_news, name='request_news'),
    path('delete_request_news/<int:news_id>', views.delete_request_news, name='delete_request_news'),

]
