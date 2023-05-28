from django.urls import path
from student import views

urlpatterns = [
    path('index', views.index),
    path('AllCourseTable',views.AllCourseTable),
    path('MyCourseTable',views.MyCourseTable),
    path('homepage', views.homepage),
    path('timetable', views.timetable),
    path('learning_process',views.learning_process)
]
