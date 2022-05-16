
from django.urls import include, path
from django.contrib import admin
urlpatterns = [
    # Defaults and Thirdparty
    path('admin/', admin.site.urls),
    path('social-auth/',include('social_django.urls',namespace='social')),
    
    
    # Custom App urls
    path('',include('accounts.urls')),
    path('admins/',include('admins.urls') ),
    path('editors/',include('editors.urls')),
    path('users/',include('users.urls')),
    
]
