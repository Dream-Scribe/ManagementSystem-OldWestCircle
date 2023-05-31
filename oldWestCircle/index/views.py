from django.shortcuts import render, HttpResponse
from index.models import Course, Teacher, Student
from index.utils import check_login, check_register, set_login_session
from utils import translateTypeId2Type

import json

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
        user = check_login(phone_number, password, temp_type)
        print(user)

        if user == 'student':
            obj = HttpResponse('学生登入成功')
            # # session 设置
            # session_id = set_login_session(phone_number, 'student')
            # obj.set_cookie("my_session_id", session_id)
            return obj
        elif user == 'teacher':
            obj = HttpResponse('教师登入成功')
            # # session 设置
            # session_id = set_login_session(phone_number, 'teacher')
            # obj.set_cookie("my_session_id", session_id)
            return obj
        else:
            return HttpResponse("失败")

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
    if request.method == 'POST':
        temp_condition = request.POST.get('temp_condition')

        course_data = Course.objects.all()

        data = []
        count = len(course_data)
        for each_data in course_data:
            temp_data = {
                'course_type': translateTypeId2Type(each_data.coursetype),
                'start_time': each_data.coursestarttime.strftime('%Y-%m-%d %X'),
                'end_time': each_data.courseendtime.strftime('%Y-%m-%d %X'),
                'course_intro': each_data.courseintro,
                'course_name': each_data.coursename,
            }
            data.append(temp_data)

        # 将结果列表转换为JSON字符串
        json_data = {
            'code': 0,
            'msg': '',
            'count': count,
            'data': data
        }
        json_data = json.dumps(json_data)

        return HttpResponse(json_data, content_type='application/json')

    return HttpResponse('this is 浏览课程列表')


def select_teacher(request):
    """
    浏览教师信息
    @param request:
    @return:
    """
    if request.method == 'POST':
        temp_condition = request.POST.get('temp_condition')

        teacher_data = Teacher.objects.all()

        data = []
        count = len(teacher_data)
        for each_data in teacher_data:
            temp_data = {
                'real_name': str(each_data.realname),
                'intro': str(each_data.teacherintro),
                'field': translateTypeId2Type(each_data.teacherfield),
                'welcome_deg': str(each_data.teacherwelcomedeg),
            }
            data.append(temp_data)

        # 将结果列表转换为JSON字符串
        json_data = {
            'code': 0,
            'msg': '',
            'count': count,
            'data': data
        }
        json_data = json.dumps(json_data)

        return HttpResponse(json_data, content_type='application/json')
    return HttpResponse('this is 浏览教师信息')


def register(request):
    """
    学生注册
    @param request:
    @return:
    """
    if request.method == 'POST':
        uuid = request.POST['temp_uuid']
        real_name = request.POST['temp_real_name']
        phone_number = request.POST['temp_number']
        user_password = request.POST['temp_password']

        result = check_register(uuid, real_name, phone_number, user_password)

        return HttpResponse(result)

    return render(request, 'register.html')
