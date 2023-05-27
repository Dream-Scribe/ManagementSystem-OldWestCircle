from django.shortcuts import render, HttpResponse
from index.models import Homework, Booking, Teachertostudentcomment, Teach

import json


# Create your views here.
def index(request):
    # return HttpResponse("this is a test")
    return render(request,'teacher/index.html')

def courseTable(request):
    return render(request,'teacher/courseTable.html')

def applyTable(request):
    return render(request,'teacher/applyTable.html')

def studentTable(request):
    return render(request,'teacher/studentTable.html')

def homepage(request):
    return render(request,'teacher/homepage.html')


def homework_assign(request):
    """
    作业发布
    @param request:
    @return:
    """
    # GET请求, 进入作业发布页面
    if request.method == 'GET':
        return render(request, 'temp_作业发布')

    # POST请求, 业务实现
    elif request.method == 'POST':
        # temp_class = request.POST.get('temp_class')
        # temp_teacher = request.POST.get('temp_teacher')
        # temp_start_time = request.POST.get('temp_start_time')
        # temp_end_time = request.POST.get('temp_end_time')
        #
        temp_class = 1
        temp_teacher = 2
        temp_start_time = 1
        temp_end_time = 1

        # # 参数不全, 错误
        # if not all([temp_name, temp_time]):
        #     return HttpResponse('参数不全')

        Homework.objects.create(classid=temp_class,
                                teacherid=temp_teacher,
                                homeworkstarttime=temp_start_time,
                                homeworkendtime=temp_end_time)


        return HttpResponse('success')

    return HttpResponse('作业发布')


def booking_select(request):
    """
    查看学员申请（预约功能）
    @param request:
    @return:
    """
    # GET请求, 进入学员申请审核页面
    if request.method == 'GET':
        return render(request, 'temp_学员申请审核')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_condition_1 = request.POST.get('temp_condition_1')
        temp_condition_2 = request.POST.get('temp_condition_2')

        # print(temp_condition_1)
        # print(temp_condition_2)

        # 列表存储查询结果
        temp_json_data = []

        # 参数都为空, 查询全部申请信息
        if not any([temp_condition_1, temp_condition_2]):
            # 执行中间表的查询操作，获取数据
            booking_data = Booking.objects.all()

            # 构建结果列表
            result = []
            for st_data in booking_data:
                student_name = st_data.studentid.realname
                teacher_name = st_data.teacherid.realname
                result.append({
                    'student_name': student_name,
                    'teacher_name': teacher_name
                })

            # 将结果列表转换为JSON字符串
            temp_json_data = json.dumps(result)

        # else:
        #     多条件动态查询
        #     temp_data 保存
        #     数组转为 json 格式

        return HttpResponse(temp_json_data, content_type='application/json')

    # return HttpResponse('预约查询')


def booking_examine(request):
    """
    审核学员申请（预约功能）
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_t_id = request.POST.get('temp_name')
        temp_s_id = request.POST.get('temp_sname')
        temp_choose = request.POST.get('temp_choose')

        # # 参数不全, 错误
        # if not all([temp_name, temp_time]):
        #     return HttpResponse('参数不全')

        if temp_choose == 1:
            Booking.objects.filter(studentid=temp_s_id, teacherid=temp_t_id).update(booksuccess=temp_choose)
        else:
            Booking.objects.filter(studentid=temp_s_id, teacherid=temp_t_id).update(booksuccess=0)

        return HttpResponse('ok')

    # return HttpResponse('预约审核')


def evaluate(request):
    """
    给予学员评价
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_studentid = request.POST.get('temp_name')
        temp_tid = request.POST.get('temp_time')
        temp_comment = request.POST.get('temp_time')

        # # 参数不全, 错误
        # if not all([temp_name, temp_time]):
        #     return HttpResponse('参数不全')

        # 添加数据到相应表
        Teachertostudentcomment.objects.create(
            studentid=temp_studentid,
            teacherid=temp_tid,
            t2scomment=temp_comment
        )

        return HttpResponse('ok')

    # return HttpResponse('评价')


def timetable(request):
    """
    查看课表
    @param request:
    @return:
    """
    # GET请求, 进入课表查看页面
    if request.method == 'GET':
        return render(request, 'temp_课表查看')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_condition_1 = request.POST.get('temp_condition_1')
        temp_condition_2 = request.POST.get('temp_condition_2')
        temp_teacherid = request.POST.get('temp_condition_2')

        # 列表存储查询结果
        temp_json_data = []

        # 参数都为空, 查询全部信息
        if not any([temp_condition_1, temp_condition_2]):
            # 执行中间表的查询操作，获取数据
            timetable_data = Teach.objects.filter(teacherid=temp_teacherid)

            # 构建结果列表
            result = []
            for time_data in timetable_data:
                course_name = time_data.courseid.courseintro
                result.append({
                    'teacher_name': course_name
                })

            # 将结果列表转换为JSON字符串
            temp_json_data = json.dumps(result)

        return HttpResponse(temp_json_data, content_type='application/json')

    return HttpResponse('课表')


def course_start(request):
    """
    课程开设
    @param request:
    @return:
    """
    # # GET请求, 进入课程开设页面
    # if request.method == 'GET':
    #     return render(request, 'temp_课程开设')
    #
    # # POST请求, 业务实现
    # elif request.method == 'POST':
    #     temp_name = request.POST.get('temp_name')
    #     temp_time = request.POST.get('temp_time')
    #
    #     # 参数不全, 错误
    #     if not all([temp_name, temp_time]):
    #         return HttpResponse('参数不全')
    #
    #     加入相应表中
    #
    #     返回成功信息。
    #     return HttpResponse('ok')

    return HttpResponse('开设课程')


def course_change(request):
    """
    课程更改
    @param request:
    @return:
    """
    # # GET请求, 进入课程开设页面
    # if request.method == 'GET':
    #     return render(request, 'temp_课程开设')
    #
    # # POST请求, 业务实现
    # elif request.method == 'POST':
    #     temp_name = request.POST.get('temp_name')
    #     temp_time = request.POST.get('temp_time')
    #
    #     # 参数不全, 错误
    #     if not all([temp_name, temp_time]):
    #         return HttpResponse('参数不全')
    #
    #     更改到相应表中
    #
    #     返回成功信息。
    #     return HttpResponse('ok')

    return HttpResponse('课程更改')
