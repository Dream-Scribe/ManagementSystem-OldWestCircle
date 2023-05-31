import json

from django.shortcuts import render, HttpResponse
from index.models import Activity, Admin, Announcement, Teacher, Student
from administrator.utils import *
from utils import get_current_time

# Create your views here.


def admin(request):
    return render(request,'admin/index.html')
def ContentPublishTable(request):
    return render(request,'admin/ContentPublishTable.html')
def UserManageTable(request):
    return render(request,'admin/UserManageTable.html')


def admin_login(request):
    """
    管理员登录
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        admin_name = request.POST.get('temp_name')
        password = request.POST.get('temp_password')

        # 验证登陆信息是否完整
        res = check_admin_login(admin_name, password)
        print(res)

        if res == 'ok':
            obj = HttpResponse('登录成功')
            # session 设置
            session_id = set_login_session(admin_name)
            obj.set_cookie("my_session_id", session_id)
            return obj
        else:
            return HttpResponse("失败")

    # return render(request, '登录页面')
    return HttpResponse("this is login")


def publish_activity(request):
    """
    活动发布
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_aid = request.POST.get('temp_admin_id')
        temp_stime = request.POST.get('temp_start_time')
        temp_etime = request.POST.get('temp_end_time')
        temp_content = request.POST.get('temp_content')
        temp_place = request.POST.get('temp_place')

        # 参数不全, 错误
        if not all([temp_aid, temp_stime, temp_etime, temp_content, temp_place]):
            return HttpResponse('参数不全')

        # 将信息添加到数据库，活动表。并返回成功信息。
        try:
            Activity.objects.create(adminid=Admin.objects.get(adminid=temp_aid),
                                    activitycontent=temp_content,
                                    activitystarttime=temp_stime,
                                    activityendtime=temp_etime,
                                    activityplace=temp_place)
            return HttpResponse('success')
        except Exception as e:
            print(e)
            return HttpResponse('error')

    return render(request, 'temp_活动发布页面')


def publish_announcement(request):
    """
    公告发布
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_aid = request.POST.get('temp_admin_id')
        temp_content = request.POST.get('temp_content')

        # 参数不全, 错误
        if not all([temp_aid, temp_content]):
            return HttpResponse('参数不全')

        # 将信息添加到数据库。并返回成功信息。
        try:
            Announcement.objects.create(adminid=Admin.objects.get(adminid=temp_aid),
                                    announcecontent=temp_content,
                                    announcepublishtime=get_current_time())

            return HttpResponse('success')
        except Exception as e:
            print(e)
            return HttpResponse('error')

    return HttpResponse('announcement publish')


def user_select(request):
    """
    用户查看
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_condition_1 = request.POST.get('temp_condition_1')
        temp_condition_2 = request.POST.get('temp_condition_2')

        # 参数都为空, 全部查询
        if not any([temp_condition_1, temp_condition_2]):
            all_data = Teacher.objects.all()

        data = []
        count = len(all_data)
        for each_data in all_data:
            temp_data = {
                'teacher_ID': str(each_data.teacherid),
                'register_time': each_data.registertime.strftime('%Y-%m-%d %X'),
                'real_name': each_data.realname,
                'phone_number': each_data.phonenumber,
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

    return render(request, 'temp_用户查询页面')


def user_add(request):
    """
    用户添加, 主要针对教师
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        uuid = request.POST.get('temp_teacher_id')
        real_name = request.POST.get('temp_real_name')
        phone_number = request.POST.get('temp_phone_number')
        userpd = request.POST.get('temp_userpd')
        teacher_field = request.POST.get('temp_field')

        # 参数不全, 错误
        if not all([uuid, real_name, phone_number, userpd]):
            return HttpResponse('参数不全')

        # 将信息添加到数据库。并返回成功信息。
        try:
            Teacher.objects.create(teacherid=int(uuid),
                                   registertime=get_current_time(),
                                   realname=real_name,
                                   phonenumber=phone_number,
                                   userpd=userpd,
                                   teacherfield=int(teacher_field))

            return HttpResponse('success')
        except Exception as e:
            print(e)
            return HttpResponse('error')

    return render(request, 'temp_用户添加页面')


def user_delete(request):
    """
    用户删除, 可在查询界面进行
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_id = request.POST.get('temp_id')

        # 参数不全, 错误
        if not all([temp_id]):
            return HttpResponse('参数不全')

        try:
            Teacher.objects.get(teacherid=int(temp_id)).delete()
            return HttpResponse('success')
        except Exception as e:
            print(e)
            return HttpResponse('error')

    return HttpResponse("user delete")


def student_select(request):
    """
    学生查看
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_condition_1 = request.POST.get('temp_condition_1')
        temp_condition_2 = request.POST.get('temp_condition_2')

        # 参数都为空, 全部查询
        if not any([temp_condition_1, temp_condition_2]):
            all_data = Student.objects.all()

        data = []
        count = len(all_data)
        for each_data in all_data:
            temp_data = {
                'student_ID': str(each_data.studentid),
                'register_time': each_data.registertime.strftime('%Y-%m-%d %X'),
                'real_name': each_data.realname,
                'phone_number': each_data.phonenumber,
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

    return render(request, 'temp_student查询页面')


def activity_select(request):
    """
    活动展示
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_aid = request.POST.get('temp_activity_id')

        if temp_aid:
            activities = Activity.objects.filter(activityid=temp_aid)
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

    return render(request, 'temp_活动展示')


def announcement_select(request):
    """
    公告展示
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_aid = request.POST.get('temp_announcement_id')

        if temp_aid:
            announcements = Announcement.objects.filter(announceid=temp_aid)
        else:
            announcements = Announcement.objects.all()

        data = []
        count = len(announcements)

        for announce in announcements:
            announce_id = announce.announceid
            announce_admin_id = announce.adminid
            announce_content = announce.announcecontent
            announce_time = announce.announcepublishtime
            if announce_time:
                announce_time = announce_time.strftime('%Y-%m-%d %X')

            data.append({
                'announce_id': announce_id,
                'announce_admin_id': str(announce_admin_id.adminid),
                'announce_content': announce_content,
                'announce_time': announce_time,
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

    return render(request, 'temp_公告展示')


def activity_delete(request):
    """
    活动删除
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_id = request.POST.get('temp_id')

        # 参数不全, 错误
        if not all([temp_id]):
            return HttpResponse('参数不全')

        try:
            Activity.objects.get(activityid=int(temp_id)).delete()
            return HttpResponse('success')
        except Exception as e:
            print(e)
            return HttpResponse('error')

    return HttpResponse("activity delete")


def announcement_delete(request):
    """
    公告删除
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_id = request.POST.get('temp_id')

        # 参数不全, 错误
        if not all([temp_id]):
            return HttpResponse('参数不全')

        try:
            Announcement.objects.get(announceid=int(temp_id)).delete()
            return HttpResponse('success')
        except Exception as e:
            print(e)
            return HttpResponse('error')

    return HttpResponse("announce delete")