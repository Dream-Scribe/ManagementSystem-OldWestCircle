from django.shortcuts import render, HttpResponse


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

    return HttpResponse("this is 首页")


def login(request):
    """
    登录
    @param request:
    @return:
    """
    # # GET请求, 进入登录页面
    # if request.method == 'GET':
    #     return render(request, 'temp_登录页面')
    #
    # # POST请求, 业务实现
    # elif request.method == 'POST':
    #     username = request.POST.get('temp_username')
    #     password = request.POST.get('temp_password')
    #     temp_type = request.POST.get('temp_type')
    #
    #     # 验证登陆信息是否完整
    #     if not all([username, password]):
    #         return HttpResponse("error")
    #
    #     elif temp_type == 'stu':
    #         # 验证用户是否存在，学生表取数据对比
    #         if not StudentModel.objects.filter(username=temp_username).exists():
    #             return HttpResponse('用户不存在')
    #
    #         # 判断密码是否正确，学生表取数据对比
    #         user = Student.objects.get(username=temp_username)
    #
    #         if not check_password(password, user.password):
    #             return HttpResponse('密码错误')
    #
    #         # 登录成功
    #         设置cookie或者使用其他校验方式
    #         return render(request, 'temp_学生登录成功界面')
    #
    #     elif 教师登录:
    #         # 验证用户是否存在，教师表取数据对比
    #         if not teacherModel.objects.filter(username=temp_username).exists():
    #             return HttpResponse('用户不存在')
    #
    #         # 判断密码是否正确，教师表取数据对比
    #         user = teacher.objects.get(username=temp_username)
    #
    #         if not check_password(password, user.password):
    #             return HttpResponse('密码错误')
    #
    #         # 登录成功
    #         设置cookie或者使用其他校验方式
    #         return render(request, 'temp_教师登录成功界面')
    #
    #     else:
    #         return HttpResponse('error')

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

