from django.urls import path
from teacher import views

urlpatterns = [
    path('test', views.test)
]
