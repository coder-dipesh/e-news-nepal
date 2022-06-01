from django.urls import include, path

from users import views

urlpatterns = [
    path('report_news', views.report_news, name='report_news'),
    path('about_us', views.about_us, name='about_us'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('account', views.account, name='account'),
]
