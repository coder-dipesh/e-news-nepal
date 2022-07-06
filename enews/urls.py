
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Defaults and Thirdparty
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('tinymce/', include('tinymce.urls')),



    # Custom App urls
    path('', include('accounts.urls')),
    path('admins/', include('admins.urls')),
    path('editors/', include('editors.urls')),
    path('users/', include('users.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'accounts.views.handler404'
