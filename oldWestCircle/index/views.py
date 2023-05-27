from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login

from index.models import Student, Teacher


# Create your views here.
def test(request):
    return HttpResponse("this is index test")


def index(request):
    """
    首页
    @param request:
    @return:
    """
    # return render(request, 'temp_首页')

    return render(request, 'login.html')


def my_login(request):
    """
    登录
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        phone_number = request.POST.get('temp_username')
        password = request.POST.get('temp_password')
        temp_type = request.POST.get('temp_type')

        # 验证登陆信息是否完整
        if not all([phone_number, password, temp_type]):
            return HttpResponse("error")

    # elif temp_type == 'student':
        #     try:
        #         student = Student.objects.get(phonenumber=phone_number, userpd=password)
        #     except Student.DoesNotExist:
        #         student = None
        #
        #     if student is not None:
        #         # 登录成功
        #         # login(request, student)  # 将学生标记为已登录状态
        #
        #         # return render(request, 'temp_学生登录成功界面')
        #         return HttpResponse("成功")
        #
        # elif temp_type == 'teacher':
        #     try:
        #         teacher = Teacher.objects.get(phonenumber=phone_number, userpd=password)
        #     except Teacher.DoesNotExist:
        #         teacher = None
        #
        #     if teacher is not None:
        #         # 登录成功
        #         # login(request, teacher)  # 将教师标记为已登录状态
        #
        #         # return render(request, 'temp_教师登录成功界面')
        #         return HttpResponse("成功")

    # return render(request, 'temp_登录页面')
    return HttpResponse("this is login")


def logout(request):
    """
    注销
    @param request:
    @return:
    """
    # if request.method == 'GET':
    #     # 注销操作
    #     response = HttpResponseRedirect(reverse('user:login'))
    #     response.delete_cookie('ticket')
    #     return response

    return HttpResponse("this is logout")


def select_course(request):
    """
    浏览课程列表
    @param request:
    @return:
    """
    # if request.method == 'GET':
    #     从 课程表 查询信息。
    #     return 查询数据

    return HttpResponse('this is 浏览课程列表')


def select_teacher(request):
    """
    浏览教师信息
    @param request:
    @return:
    """
    # if request.method == 'GET':
    #     从 教师表 查询信息。
    #     return 查询数据

    return HttpResponse('this is 浏览教师信息')


def register(request):
    if request.method == 'POST':
        phonenumber = request.POST['temp_username']
        userpd = request.POST['temp_password']

        # 创建用户并保存到数据库
        student = Student.objects.create_user(phonenumber=phonenumber, userpd=userpd)

        # 使用authenticate()函数进行注册后的自动登录
        user = authenticate(request, phonenumber=phonenumber, userpd=userpd)
        if user is not None:
            login(request, user)
            return HttpResponse("成功")  # 注册成功后重定向到仪表板页面
        else:
            return HttpResponse("失败")  # 登录失败则重定向到登录页面
    else:
        return render(request, 'register.html')
