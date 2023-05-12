from django.urls import path
from administrator import views

urlpatterns = [
    path('test', views.admin_test)
]
