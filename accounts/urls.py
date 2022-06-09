from accounts import views
from django.urls import path, include

urlpatterns = [
    # Socail Auth
    path('', include('django.contrib.auth.urls')),
    path('social-login', views.socialLogin, name='social-login'),


    # Login Register
    path('sign-in', views.signIn, name='sign-in'),
    path('sign-up', views.signUp, name='sign-up'),
    path('sign-out', views.signOut, name='sign-out'),
    path('viewnews/<int:news_id>', views.viewnews, name='viewnews'),
    path('likes', views.like_news, name='like_news'),

    path('delete-comment/<int:id>',
         views.deleteComment, name='delete-comment'),


    path('', views.home, name='home'),

    # Password Reset

    path('reset-password-enter-username', views.enterUsername,
         name='reset-password-enter-username'),
    path('new-password/<token>/', views.resetPassword, name='new-password'),
    path('reset-password-success', views.resetPasswordSuccess, name='reset-password-success'),



]
