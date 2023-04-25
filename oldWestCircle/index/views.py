from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    return HttpResponse("Hello 新东方-旧西圆！")
