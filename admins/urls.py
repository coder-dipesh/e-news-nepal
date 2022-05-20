from django.urls import include, path
from admins import views

urlpatterns = [
    path('', views.adminDashbaord, name='admins'),

    path('all-users', views.getUsers, name='all-users'),


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



]
