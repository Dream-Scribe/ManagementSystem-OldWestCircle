from django.shortcuts import render, HttpResponse
from index.models import Activity, Admin


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

    # return render(request, 'temp_活动发布页面')
    return HttpResponse('activity publish')


def publish_announcement(request):
    """
    公告发布
    @param request:
    @return:
    """
    # # GET请求, 进入发布页面
    # if request.method == 'GET':
    #     return render(request, 'temp_公告发布页面')
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
    #     将信息添加到数据库，公告表。并返回成功信息。
    #     return HttpResponse('success')

    return HttpResponse('announcement publish')


def user_select(request):
    """
    用户查看
    @param request:
    @return:
    """
    # # GET请求, 进入查询页面
    # if request.method == 'GET':
    #     return render(request, 'temp_用户查询页面')
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
    #     # 参数都为空, 全部查询
    #     if not any([temp_condition_1, temp_condition_2]):
    #         数据库查询，学生表
    #         数据库查询，教师表
    #         将结果数组合并
    #         temp_data 保存
    #         数组转为 json 格式
    #
    #     else:
    #         多条件动态查询
    #         temp_data 保存
    #         数组转为 json 格式
    #
    #     return HttpResponse(temp_json_data, content_type='application/json')

    return HttpResponse("user select")


def user_add(request):
    """
    用户添加, 主要针对教师
    @param request:
    @return:
    """
    # # GET请求, 进入用户添加页面
    # if request.method == 'GET':
    #     return render(request, 'temp_用户添加页面')
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
    #     将信息添加到数据库，教师表。并返回成功信息。
    #     return HttpResponse('success')

    return HttpResponse("user add")


def user_delete(request):
    """
    用户删除
    @param request:
    @return:
    """
    # 用户删除, 可在查询界面进行
    # # POST请求, 业务实现
    # if request.method == 'POST':
    #     temp_name = request.POST.get('temp_name')
    #
    #     # 参数不全, 错误
    #     if not all([temp_name]):
    #         return HttpResponse('参数不全')
    #
    #     从教师表根据条件删除。
    #     return HttpResponse('success')

    return HttpResponse("user delete")


