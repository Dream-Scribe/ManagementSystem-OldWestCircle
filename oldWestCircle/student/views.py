from django.shortcuts import render, HttpResponse


# Create your views here.
def test(request):
    # return HttpResponse("this is a test")
    return render(request, "studentTest/studentTest.html")