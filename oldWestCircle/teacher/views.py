from django.shortcuts import render, HttpResponse


# Create your views here.
def test(request):
    # return HttpResponse("this is a test")
    return HttpResponse('this is teacher')


def homework_assign(request):
    """
    作业发布
    @param request:
    @return:
    """
    # # GET请求, 进入作业发布页面
    # if request.method == 'GET':
    #     return render(request, 'temp_作业发布')
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
    #     将信息添加到数据库，作业表。并返回成功信息。
    #     return HttpResponse('success')

    return HttpResponse('作业发布')


def booking_select(request):
    """
    查看学员申请（预约功能）
    @param request:
    @return:
    """
    # # GET请求, 进入学员申请审核页面
    # if request.method == 'GET':
    #     return render(request, 'temp_学员申请审核')
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
    #     # 参数都为空, 查询全部申请信息
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

    return HttpResponse('预约查询')


def booking_examine(request):
    """
    审核学员申请（预约功能）
    @param request:
    @return:
    """
    # # POST请求, 业务实现
    # if request.method == 'POST':
    #     temp_name = request.POST.get('temp_name')
    #     temp_time = request.POST.get('temp_time')
    #
    #     # 参数不全, 错误
    #     if not all([temp_name, temp_time]):
    #         return HttpResponse('参数不全')
    #
    #     if 根据选择判断，如果同意
    #         更改预约表状态
    #     else:
    #         相应更改预约表状态
    #
    #     返回成功信息。
    #     return HttpResponse('ok')

    return HttpResponse('预约审核')


def evaluate(request):
    """
    给予学员评价
    @param request:
    @return:
    """
    # # POST请求, 业务实现
    # if request.method == 'POST':
    #     temp_name = request.POST.get('temp_name')
    #     temp_time = request.POST.get('temp_time')
    #
    #     # 参数不全, 错误
    #     if not all([temp_name, temp_time]):
    #         return HttpResponse('参数不全')
    #
    #     添加数据到相应表
    #
    #     返回成功信息。
    #     return HttpResponse('ok')

    return HttpResponse('评价')


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
    #     # 参数都为空, 查询全部申请信息
    #     if not any([temp_condition_1, temp_condition_2]):
    #         数据库相应表查询
    #         将结果数组合并
    #         temp_data 保存
    #         数组转为 json 格式
    #
    #     return HttpResponse(temp_json_data, content_type='application/json')

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
