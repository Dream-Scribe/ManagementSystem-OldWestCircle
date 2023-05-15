from django.shortcuts import render, HttpResponse

# Create your views here.


def admin_test(request):
    return HttpResponse("this is admin test")


def publish_activity(request):
    """
    活动发布
    @param request:
    @return:
    """
    pass


def publish_notice(request):
    """
    公告发布
    @param request:
    @return:
    """
    pass


def user_select(request):
    """
    用户查看
    @param request:
    @return:
    """
    pass


def user_add(request):
    """
    用户添加
    @param request:
    @return:
    """
    return HttpResponse("userAdd")


def user_delete(request):
    """
    用户删除
    @param request:
    @return:
    """
    pass


