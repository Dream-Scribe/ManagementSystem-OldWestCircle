from django.urls import path
from student import views

urlpatterns = [
    path('index', views.index),
    path('AllCourseTable', views.AllCourseTable),
    path('MyCourseTable', views.MyCourseTable),
    path('homepage', views.homepage),
    path('timetable', views.timetable),
    path('learning_process', views.learning_process),
    path('activityAttend', views.activity_attend),
    path('activityCancel', views.activity_cancel),
    path('activityShow', views.activity_show),
    path('announceShow', views.announcement_show),
    path('booking', views.booking),
    path('bookingSelect', views.booking_select),
    path('teacherEvaluate', views.evaluate_teacher),
    path('classChoose', views.class_choose),
    path('classQuit', views.class_quit)
]
