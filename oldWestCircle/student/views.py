from django.shortcuts import render, HttpResponse
import json

from django.utils import timezone
from index.models import *


# Create your views here.
def index(request):
    return render(request, 'student/index.html')


def AllCourseTable(request):
    return render(request, 'student/AllCourseTable.html')


def MyCourseTable(request):
    return render(request, 'student/MyCourseTable.html')


def homepage(request):
    return render(request, 'student/homepage.html')


def activity_attend(request):
    """
    报名活动
    @param request:
    @return:
    """
    # GET请求, 进入活动参加
    if request.method == 'GET':
        return render(request, 'temp_报名活动')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_aid = request.POST.get('temp_activity_id')
        temp_sid = request.POST.get('temp_student_id')
        print(temp_sid)
        if not all([temp_aid, temp_sid]):
            return HttpResponse('参数不全')
        elif temp_aid and temp_sid:
            attend = Studentattend.objects.create(activityid=Activity.objects.get(activityid=temp_aid),
                                                  studentid=Student.objects.get(studentid=temp_sid))
            return HttpResponse('ok')

    return HttpResponse('报名活动')


def activity_cancel(request):
    """
         取消活动
         @param request:
         @return:
    """
    # GET请求, 进入活动取消
    if request.method == 'GET':
        return render(request, 'temp_活动取消')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_aid = request.POST.get('temp_activity_id')
        temp_sid = request.POST.get('temp_student_id')

        if not all([temp_aid, temp_sid]):
            return HttpResponse('参数不全')
        elif temp_aid and temp_sid:
            Studentattend.objects.filter(activityid=temp_aid, studentid=temp_sid).delete()

            return HttpResponse('ok')

    return HttpResponse('活动取消')


def activity_show(request):
    """
             活动展示
             @param request:
             @return:
    """
    # GET请求, 进入活动展示
    if request.method == 'GET':
        return render(request, 'temp_活动展示')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_aid = request.POST.get('temp_activity_id')
        temp_sid = request.POST.get('temp_student_id')

        if temp_aid and temp_sid:
            activities = [Studentattend.objects.get(activityid=temp_aid, studentid=temp_sid).activityid]
        elif temp_sid:
            activities = [x.activityid for x in Studentattend.objects.filter(studentid=temp_sid)]
        else:
            activities = Activity.objects.all()

        data = []
        count = len(activities)

        for activity in activities:
            activity_id = activity.activityid
            activity_content = activity.activitycontent
            activity_place = activity.activityplace
            activity_stime = activity.activitystarttime
            if activity_stime:
                activity_stime = activity_stime.strftime('%Y-%m-%d %X')

            activity_etime = activity.activityendtime
            if activity_etime:
                activity_etime = activity_etime.strftime('%Y-%m-%d %X')
            data.append({
                'activity_id': activity_id,
                'content': activity_content,
                'place': activity_place,
                'start_time': activity_stime,
                'end_time': activity_etime,
            })

        # 将结果列表转换为JSON字符串
        json_data = {
            'code': 0,
            'msg': '',
            'count': count,
            'data': data
        }
        json_data = json.dumps(json_data)

        return HttpResponse(json_data, content_type='application/json')


def announcement_show(request):
    """
            公告展示
            @param request:
            @return:
    """
    # GET请求, 进入活动展示
    if request.method == 'GET':
        return render(request, 'temp_活动展示')

    # POST请求, 业务实现
    elif request.method == 'POST':
        announcements = Announcement.objects.all()

        data = []
        count = len(announcements)
        for announcement in announcements:
            announcement_id = announcement.announceid
            content = announcement.announcecontent
            time = announcement.announcepublishtime
            if time:
                time = time.strftime('%Y-%m-%d %X')
            data.append({
                'announcement_id': announcement_id,
                'content': content,
                'publish_time': time
            })

        # 将结果列表转换为JSON字符串
        json_data = {
            'code': 0,
            'msg': '',
            'count': count,
            'data': data
        }
        json_data = json.dumps(json_data)

        return HttpResponse(json_data, content_type='application/json')


def booking(request):
    """
    预约老师
    @param request:
    @return:
    """
    # GET请求, 进入预约申请页面
    if request.method == 'GET':
        return render(request, 'temp_申请')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_sid = request.POST.get('temp_student_id')
        temp_tid = request.POST.get('temp_teacher_id')
        temp_time = request.POST.get('temp_time')
        temp_place = request.POST.get('temp_place')
        temp_description = request.POST.get('temp_description')

        # 参数不全, 错误
        if not all([temp_sid, temp_tid, temp_time, temp_place]):
            return HttpResponse('参数不全')

        # 先判断时间是否冲突
        booking = Booking.objects.filter(teacherid=temp_tid, booktime=temp_time)
        if booking:
            return HttpResponse('冲突')
        # 添加数据到相应表
        Booking.objects.create(studentid=Student.objects.get(studentid=temp_sid),
                               teacherid=Teacher.objects.get(teacherid=temp_tid), booktime=temp_time,
                               bookplace=temp_place,
                               bookdescription=temp_description, booksuccess=0)
        # 返回成功信息。
        return HttpResponse('ok')

    return HttpResponse('预约老师')


def booking_valid(request):
    """
        检测预约是否冲突
        @param request:
        @return:
        """
    # GET请求, 进入预约申请页面
    if request.method == 'GET':
        return render(request, 'temp_申请')

    # POST请求, 业务实现
    elif request.method == 'POST':
        # temp_sid = request.POST.get('temp_student_id')
        temp_tid = request.POST.get('temp_teacher_id')
        temp_time = request.POST.get('temp_time')
        booking = Booking.objects.filter(teacherid=temp_tid, booktime=temp_time)
        if booking:
            return HttpResponse('冲突')
        else:
            return HttpResponse('ok')


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

        temp_tid = request.POST.get('temp_teacher_id')
        temp_sid = request.POST.get('temp_student_id')
        temp_time = request.POST.get('temp_time')

        # 参数都为空, 查询全部申请信息 必须有学生id

        if temp_tid and temp_time and temp_sid:
            booking_data = Booking.objects.filter(teacherid=temp_tid, studentid=temp_sid, booktime=temp_time)
        elif temp_sid and temp_tid:
            booking_data = Booking.objects.filter(teacherid=temp_tid, studentid=temp_sid)
        elif temp_time and temp_sid:
            booking_data = Booking.objects.filter(studentid=temp_sid,
                                                  booktime=temp_time)
        elif temp_sid:
            booking_data = Booking.objects.filter(studentid=temp_sid)
        else:
            return HttpResponse('参数不全')
        # 构建结果列表
        data = []
        count = len(booking_data)
        for st_data in booking_data:
            student_name = st_data.studentid.realname
            teacher_name = st_data.teacherid.realname
            bookdescription = st_data.bookdescription
            time = st_data.booktime
            if time:
                time = time.strftime('%Y-%m-%d %X')
            data.append({
                'student_name': student_name,
                'teacher_name': teacher_name,
                'bookdescription': bookdescription,
                'time': time

            })

        # 将结果列表转换为JSON字符串
        json_data = {
            'code': 0,
            'msg': '',
            'count': count,
            'data': data
        }
        json_data = json.dumps(json_data)

        return HttpResponse(json_data, content_type='application/json')

    # return HttpResponse('预约查询')


def timetable(request):
    """
    查看课表
    @param request:
    @return:
    """
    # # GET请求, 进入课表查看页面
    # if request.method == 'GET':
    #     return render(request, 'temp_课表查看')
    #
    # # POST请求, 业务实现
    # elif request.method == 'POST':
    #     temp_condition_1 = request.POST.get('temp_condition_1')
    #     temp_condition_2 = request.POST.get('temp_condition_2')
    #
    #     # 列表存储查询结果
    #     temp_data = []
    #     temp_json_data = []
    #
    #     # 参数都为空, 查询全部信息
    #     if not any([temp_condition_1, temp_condition_2]):
    #         数据库相应表查询
    #         将结果数组合并
    #         temp_data 保存
    #         数组转为 json 格式
    #
    #     return HttpResponse(temp_json_data, content_type='application/json')

    return HttpResponse('课表')


def learning_process(request):
    """
    学习历程
    @param request:
    @return:
    """
    # # GET请求, 进入学习历程查看页面
    # if request.method == 'GET':
    #     return render(request, 'temp_学习历程')
    #
    # # POST请求, 业务实现
    # elif request.method == 'POST':
    #     temp_name = request.POST.get('temp_name')
    #     temp_time = request.POST.get('temp_time')
    #
    #     从相应表获取数据
    #
    #     返回数据。
    #
    #     return HttpResponse('temp_data')

    return HttpResponse('学习历程')


def evaluate_teacher(request):
    """
    给予教师评价
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_tid = request.POST.get('temp_teacher_id')
        temp_sid = request.POST.get('temp_student_id')

        temp_comment = request.POST.get('temp_comment')
        temp_star = request.POST.get('temp_star')
        time = timezone.now()

        # 参数不全, 错误

        if not all([temp_sid, temp_tid]):
            return HttpResponse('参数不全')

            # 添加数据到相应表
        Studenttoteachercomment.objects.create(
            studentid=Student.objects.get(studentid=temp_sid),
            teacherid=Teacher.objects.get(teacherid=temp_tid),
            s2tcomment=temp_comment,
            s2tstar=temp_star,
            s2tcommenttime=time
        )
        # 返回成功信息。
        return HttpResponse('ok')

    return HttpResponse('这是学生给教师评价')

