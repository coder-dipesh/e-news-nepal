from django.urls import include, path

from users import views

urlpatterns = [
    path('report_news', views.report_news, name='report_news'),
    path('view_news', views.view_news, name='view_news'),
    path('about_us', views.about_us, name='about_us'),
]
