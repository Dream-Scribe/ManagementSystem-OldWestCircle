from django.shortcuts import render, HttpResponse
import json

from django.utils import timezone
from index.models import *
from utils import *


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
            book_description = st_data.bookdescription
            time = st_data.booktime
            if time:
                time = time.strftime('%Y-%m-%d %X')
            data.append({
                'student_name': student_name,
                'teacher_name': teacher_name,
                'book_description': book_description,
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
    # GET请求, 进入课表查看页面
    if request.method == 'GET':
        return render(request, 'temp_课表查看')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_sid = request.POST.get('temp_student_id')

        # 参数都为空, 查询全部信息
        if not temp_sid:
            return HttpResponse("参数不全")
        else:
            timetable_data = Studyingat.objects.filter(studentid=temp_sid)
        data = []
        count = len(timetable_data)
        # 数据库相应表查询
        for time_data in timetable_data:
            class_id = time_data.classid
            course_name = class_id.courseid.coursename
            course_type = class_id.courseid.coursetype
            course_type = translateTypeId2Type(course_type)
            stime = class_id.courseid.coursestarttime
            etime = class_id.courseid.courseendtime
            if stime:
                stime = stime.strftime('%Y-%m-%d %X')

            if etime:
                etime = etime.strftime('%Y-%m-%d %X')
            time = class_id.classtime
            date = translateDateId2Date(class_id.classdate)
            data.append({
                'class_id': class_id.classid,
                'course_name': course_name,
                'class_time': time,
                'class_date': date,
                'course_start_time': stime,
                'course_end_time': etime,
                'course_type': course_type
            })
        # 数组转为 json 格式
        json_data = {
            'code': 0,
            'msg': '',
            'count': count,
            'data': data
        }
        json_data = json.dumps(json_data)

        return HttpResponse(json_data, content_type='application/json')

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
        comment = Studenttoteachercomment.objects.get(
            studentid=Student.objects.get(studentid=temp_sid),
            teacherid=Teacher.objects.get(teacherid=temp_tid)
        )
        if comment is None:
            Studenttoteachercomment.objects.create(
                studentid=Student.objects.get(studentid=temp_sid),
                teacherid=Teacher.objects.get(teacherid=temp_tid),
                s2tstar=temp_star,
                s2tcomment=temp_comment,
                s2tcommenttime=time
            )
        else:
            comment.update(s2tstar=temp_star,
                s2tcomment=temp_comment,
                s2tcommenttime=time)
        # 返回成功信息。
        return HttpResponse('ok')

    return HttpResponse('这是学生给教师评价')


def teacher_eval_delete(request):
    """
       删除已有的对教师的评价
       @param request:
       @return:
       """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_tid = request.POST.get('temp_teacher_id')
        temp_sid = request.POST.get('temp_student_id')


        if not all([temp_sid, temp_tid]):
            return HttpResponse('参数不全')
        Studenttoteachercomment.objects.filter(studentid=Student.objects.get(studentid=temp_sid),
                                               teacherid=Teacher.objects.get(teacherid=temp_tid)
                                               ).delete()
        return HttpResponse('ok')


def class_choose(request):
    """
           选择班级
           @param request:
           @return:
           """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_sid = request.POST.get('temp_student_id')
        temp_cid = request.POST.get('temp_class_id')

        if not any([temp_sid, temp_cid]):
            return HttpResponse('参数不全')

        class_ = Class.objects.get(classid=temp_cid)
        if class_ is None:
            return HttpResponse('不存在该班级')
        record = Studyingat.objects.get(classid=class_, studentid=temp_sid)
        if record is None:
            Studyingat.objects.create(classid=class_, studentid=Student.objects.get(studentid=temp_sid))
            class_.update(classstudentnum=class_.classstudentnum + 1)
            class_.courseid.update(courseregisternum=class_.courseid.courseregisternum + 1)
        else:
            return HttpResponse('已经在该班级')

        return HttpResponse('ok')
    return HttpResponse('选择班级')


def class_quit(request):
    """
               退出一个班级
               @param request:
               @return:
               """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_sid = request.POST.get('temp_student_id')
        temp_cid = request.POST.get('temp_class_id')

        if not any([temp_sid, temp_cid]):
            return HttpResponse('参数不全')
        record = Studyingat.objects.get(classid=temp_cid, studentid=temp_sid)
        if record is not None:
            class_ = record.classid
            class_.update(classstudentnum=class_.classstudentnum - 1)
            class_.courseid.update(courseregisternum=class_.courseid.courseregisternum - 1)
            record.delete()

            return HttpResponse('ok')
        else:
            return HttpResponse('不在该班级')

    return HttpResponse('退出班级')


def homework_select(request):
    """
     查看发布的作业
     @param request:
     @return:
     """
    # GET请求, 进入作业发布
    if request.method == 'GET':
        return render(request, 'temp_作业发布')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_hid = request.POST.get('temp_homework_id')
        temp_cid = request.POST.get('temp_class_id')
        temp_tid = request.POST.get('temp_teacher_id')

        # 参数都为空, 查询全部申请信息
        if not temp_tid:
            # 执行中间表的查询操作，获取数据
            homework_data = Homework.objects.all()
        elif temp_hid and temp_cid:
            homework_data = Homework.objects.filter(teacherid=temp_tid, homeworkid=temp_hid, classid=temp_cid)
        elif temp_hid:
            homework_data = Homework.objects.filter(teacherid=temp_tid, homeworkid=temp_hid)
        elif temp_cid:
            homework_data = Homework.objects.filter(teacherid=temp_tid, classid=temp_cid)
        else:
            homework_data = Homework.objects.filter(teacherid=temp_tid)

        # 构建结果列表
        data = []
        count = len(homework_data)
        for hw_data in homework_data:
            class_id = hw_data.classid

            homework_id = hw_data.homeworkid

            course_name = hw_data.classid.courseid.coursename
            stime = hw_data.homeworkstarttime
            if stime:
                stime = stime.strftime('%Y-%m-%d %X')
            etime = hw_data.homeworkendtime.strftime('%Y-%m-%d %X')
            # if etime:
            #     etime = etime.strftime('%Y-%m-%d %X')
            content = hw_data.homeworkcontent
            data.append({
                'homework_id': homework_id,
                'class_id': class_id.classid,
                'course_name': course_name,
                'start_time': stime,
                'end_time': etime,
                'content': content
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


def evaluate_course(request):
    """
    给予课程评价
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_cid = request.POST.get('temp_course_id')
        temp_sid = request.POST.get('temp_student_id')

        temp_comment = request.POST.get('temp_comment')
        temp_star = request.POST.get('temp_star')
        time = timezone.now()

        # 参数不全, 错误

        if not all([temp_sid, temp_cid]):
            return HttpResponse('参数不全')

            # 添加数据到相应表
        comment = Studenttocoursecomment.objects.filter(
            studentid=Student.objects.get(studentid=temp_sid),
            courseid=Course.objects.get(courseid=temp_cid)
        )
        print(comment.count())
        # 只允许评价一次，再次评价会覆盖上一次
        if comment.count() == 0:
            Studenttocoursecomment.objects.create(
                studentid=Student.objects.get(studentid=temp_sid),
                courseid=Course.objects.get(courseid=temp_cid),
                s2ccomment=temp_comment,
                s2cstar=temp_star,
                s2ccommenttime=time
            )
            return HttpResponse('ok')

        else:
            comment.update(
                s2ccomment=temp_comment,
                s2cstar=temp_star,
                s2ccommenttime=time
            )
            # 返回成功信息。
            return HttpResponse('已覆盖上一次的评论')

    return HttpResponse('课程评价')


def course_eval_delete(request):
    """
       删除已有的对课程的评价
       @param request:
       @return:
       """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_cid = request.POST.get('temp_course_id')
        temp_sid = request.POST.get('temp_student_id')

        if not all([temp_sid, temp_cid]):
            return HttpResponse('参数不全')
        comment = Studenttocoursecomment.objects.filter(
            studentid=Student.objects.get(studentid=temp_sid),
            courseid=Course.objects.get(courseid=temp_cid)
        )
        if comment:
            comment.delete()

        return HttpResponse('ok')


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
