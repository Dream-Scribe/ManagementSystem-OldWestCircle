from django.urls import path
from student import views

urlpatterns = [
    path('index', views.index),
    path('AllCourseTable',views.AllCourseTable),
    path('MyCourseTable',views.MyCourseTable),
    path('homepage', views.homepage),
    path('admin', views.admin),
    path('ContentPublishTable',views.ContentPublishTable),
    path('UserManageTable',views.UserManageTable)
]
