from django.urls import include, path
from admins import views

urlpatterns = [
    # Admin dashboard
    path('', views.adminDashbaord, name='admins'),

    # Show all users``
    path('all-users', views.getUsers, name='all-users'),

    # Admin CRUD on editors.
    path('all-editors', views.getEditor, name='all-editors'),
    path('editor-sign-up', views.editorSignUp, name='editor-sign-up'),
    path('remove-editor/<int:editor_id>',
         views.removeEditor, name='remove-editor'),
    path('update-editor/<int:editor_id>',
         views.updateEditor, name='update-editor'),


    # This is url for the Category
    path('all-category', views.getCategory, name='all-category'),
    path('new-category', views.newCategory, name='new-category'),

    path('delete_category/<int:P_id>',
         views.delete_category, name='delete_category'),

    path('update_category/<str:p_id>',
         views.update_category, name='update_category'),

    path('categoryupdatebutton', views.categoryupdatebutton,
         name='categoryupdatebutton'),
    # THis is url for the all news
    path('all-news', views.getNews, name='all-news'),

    # THis is url for the Site Setting
    path('siteSetting', views.SiteSettingss, name='siteSetting'),

    path('all-contacts', views.allContact, name='all-contacts'),



]
