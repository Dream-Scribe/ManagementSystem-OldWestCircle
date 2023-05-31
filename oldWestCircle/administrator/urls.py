from django.urls import path
from administrator import views

urlpatterns = [
    path('test', views.admin_test),
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
    path('admin', views.admin),
    path('ContentPublishTable',views.ContentPublishTable),
    path('UserManageTable',views.UserManageTable),
]
