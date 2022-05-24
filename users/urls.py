from django.urls import include, path

from users import views

urlpatterns = [
    path('report_news', views.report_news, name='report_news'),
]