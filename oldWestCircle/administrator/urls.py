from django.urls import path
from administrator import views

urlpatterns = [
    path('test', views.admin_test),
    path('activity', views.publish_activity),
    path('announcement', views.publish_announcement),
    path('userSelect', views.user_select),
    path('userAdd', views.user_add),
    path('userDelete', views.user_delete),
]
