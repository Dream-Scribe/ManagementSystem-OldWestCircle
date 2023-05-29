import json

from django.shortcuts import render, HttpResponse
from index.models import Activity, Admin, Announcement, Teacher


# Create your views here.


def admin_test(request):
    return HttpResponse("this is admin test")

def admin(request):
    return render(request,'admin/index.html')
def ContentPublishTable(request):
    return render(request,'admin/ContentPublishTable.html')
def UserManageTable(request):
    return render(request,'admin/UserManageTable.html')


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
        temp_time = request.POST.get('temp_time')

        # 参数不全, 错误
        if not all([temp_aid, temp_time, temp_content]):
            return HttpResponse('参数不全')

        # 将信息添加到数据库。并返回成功信息。
        try:
            Announcement.objects.create(adminid=Admin.objects.get(adminid=temp_aid),
                                    announcecontent=temp_content,
                                    announcepublishtime=temp_time)

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
        teacher_id = request.POST.get('temp_teacher_id')
        register_time = request.POST.get('temp_register_time')
        real_name = request.POST.get('temp_real_name')
        phone_number = request.POST.get('temp_phone_number')
        userpd = request.POST.get('temp_userpd')
        teacher_field = int(request.POST.get('teacher_field'))

        # 参数不全, 错误
        if not all([teacher_id, real_name, phone_number, userpd]):
            return HttpResponse('参数不全')

        # 将信息添加到数据库。并返回成功信息。
        try:
            Teacher.objects.create(teacherid=int(teacher_id),
                                   registertime=register_time,
                                   realname=real_name,
                                   phonenumber=phone_number,
                                   userpd=userpd,
                                   teacherfield=teacher_field)

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
        temp_id = int(request.POST.get('temp_id'))

        # 参数不全, 错误
        if not all([temp_id]):
            return HttpResponse('参数不全')

        try:
            Teacher.objects.get(teacherid=temp_id).delete()
            return HttpResponse('success')
        except Exception as e:
            print(e)
            return HttpResponse('error')

    return HttpResponse("user delete")


