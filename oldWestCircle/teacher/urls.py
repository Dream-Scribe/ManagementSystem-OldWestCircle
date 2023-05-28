from django.urls import path
from teacher import views

urlpatterns = [
    path('index', views.index),
    path('courseTable', views.courseTable),
    path('applyTable', views.applyTable),
    path('studentTable', views.studentTable),
    path('homepage', views.homepage),
    path('homework', views.homework),
    path('bookingSelect', views.booking_select),
    path('bookingExamine', views.booking_examine),
    path('evaluate', views.evaluate),
    path('timetable', views.timetable),
    path('courseStart', views.course_start),
    path('courseChange', views.course_change),
    path('courseDelete', views.course_delete),
    path('homeworkAssign', views.homework_assign),
    path('homeworkChange', views.homework_change),
    path('homeworkDelete', views.homework_delete),
    path('homeworkSelect', views.homework_select),
    path('activityShow', views.activity_show),
    path('activityAttend', views.activity_attend),
    path('activityCancel', views.activity_cancel),
    path('announceShow', views.announcement_show)
]
