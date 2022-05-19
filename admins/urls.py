from django.urls import include, path
from admins import views

urlpatterns = [
    path('', views.adminDashbaord, name='admins'),

    path('all-users', views.getUsers, name='all-users'),


    path('all-editors', views.getEditor, name='all-editors'),
    path('editor-sign-up', views.editorSignUp, name='editor-sign-up'),
    path('remove-editor/<int:editor_id>', views.removeEditor, name='remove-editor'),
    path('update-editor/<int:editor_id>', views.updateEditor, name='update-editor'),
    
    


    # This is url for the Category
    path('all-category', views.getCategory, name='all-category'),
    path('new-category', views.newCategory, name='new-category'),




]
