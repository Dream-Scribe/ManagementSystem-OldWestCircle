from django.urls import path
from student import views

urlpatterns = [
    path('index', views.index),
    path('AllCourseTable', views.AllCourseTable),
    path('MyCourseTable', views.MyCourseTable),
    path('teacherTable', views.teacherTable),
    path('activityTable_stu', views.activityTable_stu),
    path('announcementTable_stu', views.announcementTable_stu),
    path('addpage_activity_stu',views.addpage_activity_stu),
    path('addpage_teacherBooking',views.addpage_teacherBooking),
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
    path('teacherEvalDelete', views.teacher_eval_delete),
    path('classChoose', views.class_choose),
    path('classQuit', views.class_quit),
    path('homeworkSelect', views.homework_select),
    path('courseEvaluate', views.evaluate_course),
    path('teacherSelect', views.select_teacher),
    path('classSelect', views.class_select),
    path('courseEvalDelete', views.course_eval_delete)
]
