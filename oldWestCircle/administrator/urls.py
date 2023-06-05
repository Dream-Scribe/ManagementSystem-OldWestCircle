from django.urls import path
from administrator import views

urlpatterns = [
    path('',views.admin_loginPage),
    path('login', views.admin_login),
    path('activity', views.publish_activity),
    path('activityShow', views.activity_select),
    path('announcementShow', views.announcement_select),
    path('announcement', views.publish_announcement),
    path('userSelect', views.user_select),
    path('studentSelect', views.student_select),
    path('userAdd', views.user_add),
    path('userDelete', views.user_delete),
    path('activityDelete', views.activity_delete),
    path('announcementDelete', views.announcement_delete),
    path('index', views.index),
    path('ContentPublishTable',views.ContentPublishTable),
    path('UserManageTable',views.UserManageTable),
    path('activityTable',views.activityTable),
    path('announcementTable',views.announcementTable),
    path('addpage_activity',views.addpage_activity),
    path('addpage_announcement',views.addpage_announcement),
    path('addpage_user',views.addpage_user),
    path('addpageTest',views.addpageTest)
]
