from django.shortcuts import render, HttpResponse

# Create your views here.


def admin_test(request):
    return HttpResponse("this is admin test")

