from django.urls import path
from teacher import views

urlpatterns = [
    path('index', views.index),
    path('courseTable',views.courseTable),
    path('applyTable',views.applyTable),
    path('studentTable',views.studentTable),
    path('homepage',views.homepage),
    path('homework', views.homework_assign),
    path('bookingSelect', views.booking_select),
    path('bookingExamine', views.booking_examine),
    path('evaluate', views.evaluate),
    path('timetable', views.timetable),
    path('courseStart', views.course_start),
    path('courseChange', views.course_change),
    path('courseDelete',views.course_delete)

]
