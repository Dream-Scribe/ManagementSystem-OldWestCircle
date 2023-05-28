from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request,'student/index.html')

def AllCourseTable(request):
    return render(request,'student/AllCourseTable.html')

def MyCourseTable(request):
    return render(request,'student/MyCourseTable.html')

def homepage(request):
    return render(request,'student/homepage.html')

def sign_up_activity(request):
    """
    报名活动
    @param request:
    @return:
    """
    return HttpResponse('报名活动')


def booking(request):
    """
    预约老师
    @param request:
    @return:
    """
    # # GET请求, 进入预约申请页面
    # if request.method == 'GET':
    #     return render(request, 'temp_申请')
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
    #     先判断时间是否冲突
    #
    #     添加数据到相应表
    #
    #     返回成功信息。
    #     return HttpResponse('ok')

    return HttpResponse('预约老师')


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

    return HttpResponse('这是学生给教师评价')


