from django.urls import path
from index import views

urlpatterns = [
    path('test', views.test),
    path('', views.index),
    path('login', views.login),
    path('logout', views.logout),
    path('course', views.select_course),
    path('teacher', views.select_teacher),

]
