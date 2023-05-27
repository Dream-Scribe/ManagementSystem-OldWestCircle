from django.urls import path
from student import views

urlpatterns = [
    path('test', views.test),
    path('homepage', views.homepage)
]
