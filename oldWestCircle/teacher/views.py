from django.utils import timezone
import json

from django.shortcuts import render, HttpResponse
from index.models import *
from utils import *


# Create your views here.
def index(request):
    # return HttpResponse("this is a test")
    return render(request, 'teacher/index.html')


def courseTable(request):
    return render(request, 'teacher/courseTable.html')


def applyTable(request):
    return render(request, 'teacher/applyTable.html')


def studentTable(request):
    return render(request, 'teacher/studentTable.html')


def homepage(request):
    return render(request, 'teacher/homepage.html')

def addPage(request):
    return render(request, 'teacher/addPage.html')

def homework(request):
    return render(request, 'teacher/homework.html')

def addHomework(request):
    return render(request, 'teacher/addHomework.html')

def activityTable(request):
    return render(request, 'teacher/activityTable.html')

def announcementTable(request):
    return render(request, "teacher/announcementTable.html")

def classTable(request):
    return render(request,"teacher/classTable.html")

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

        # 参数都为空, 查询全部申请信息
        if not temp_tid:

            # 执行中间表的查询操作，获取数据
            booking_data = Booking.objects.all()
        elif temp_sid and temp_time:

            booking_data = Booking.objects.filter(teacherid=temp_tid, studentid=temp_sid, bookingtime=temp_time)
        elif temp_sid:
            booking_data = Booking.objects.filter(teacherid=temp_tid, studentid=temp_sid)
        elif temp_time:
            booking_data = Booking.objects.filter(teacherid=temp_tid,
                                                  bookingtime=temp_time)
        else:
            booking_data = Booking.objects.filter(teacherid=temp_tid)

        # 构建结果列表
        data = []
        count = len(booking_data)
        for st_data in booking_data:
            student_id = st_data.studentid.studentid
            student_name = st_data.studentid.realname
            teacher_id = st_data.teacherid.teacherid
            teacher_name = st_data.teacherid.realname
            bookdescription = st_data.bookdescription
            time = st_data.booktime
            if time:
                time = time.strftime('%Y-%m-%d %X')
            data.append({
                'student_id': student_id,
                'student_name': student_name,
                'teacher_id': teacher_id,
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


def booking_examine(request):
    """
    审核学员申请（预约功能）
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_tid = request.POST.get('temp_tid')
        temp_sid = request.POST.get('temp_sid')
        temp_choose = request.POST.get('temp_choose')

        # 参数不全, 错误
        if not all([temp_sid, temp_tid]):
            return HttpResponse('参数不全')

        if temp_choose == '1':
            Booking.objects.filter(studentid=temp_sid, teacherid=temp_tid).update(booksuccess=1)
        else:
            Booking.objects.filter(studentid=temp_sid, teacherid=temp_tid).update(booksuccess=0)

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
        temp_studentid = request.POST.get('temp_sid')
        temp_tid = request.POST.get('temp_tid')
        temp_comment = request.POST.get('temp_comment')
        temp_star = request.POST.get('temp_star')
        time = timezone.now()

        #  参数不全, 错误
        if not all([temp_studentid, temp_tid]):
            return HttpResponse('参数不全')

        # 添加数据到相应表
        comment = Teachertostudentcomment.objects.get(
            studentid=Student.objects.filter(studentid=temp_studentid).first(),
            teacherid=Teacher.objects.filter(teacherid=temp_tid).first(),
            t2scomment=temp_comment,
            t2sstar=temp_star,
            t2scommenttime=time
        )
        if comment:
            comment.update(t2scomment=temp_comment,
            t2sstar=temp_star,
            t2scommenttime=time)
        else:
            Teachertostudentcomment.objects.create(
                studentid=Student.objects.filter(studentid=temp_studentid).first(),
                teacherid=Teacher.objects.filter(teacherid=temp_tid).first(),
                t2scomment=temp_comment,
                t2sstar=temp_star,
                t2scommenttime=time
            )
        return HttpResponse('ok')

    # return HttpResponse('评价')
def evaluate_delete(request):
    """
       删除评价
       @param request:
       @return:
       """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_tid = request.POST.get('temp_teacher_id')
        temp_sid = request.POST.get('temp_student_id')

        temp_time = request.POST.get('temp_time')
        if not all([temp_sid, temp_tid, temp_time]):
            return HttpResponse('参数不全')
        Teachertostudentcomment.objects.filter(studentid=Student.objects.get(studentid=temp_sid),
                                               teacherid=Teacher.objects.get(teacherid=temp_tid),
                                               s2tcommenttime=temp_time).delete()
        return HttpResponse('ok')


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
        temp_tid = request.POST.get('temp_tid')

        # 参数都为空, 查询全部信息
        if not temp_tid:
            # 执行中间表的查询操作，获取数据
            timetable_data = Teach.objects.all()
        else:
            timetable_data = Teach.objects.filter(teacherid=int(temp_tid))

        # 构建结果列表
        data = []
        count = len(timetable_data)
        for time_data in timetable_data:
            course_id = time_data.courseid.courseid
            course_name = time_data.courseid.coursename
            class_set = Class.objects.filter(courseid=time_data.courseid)
            course_time = []
            for class_data in class_set:
                class_date = class_data.classdate
                class_date = translateDateId2Date(class_date)
                class_time = class_data.classtime
                course_time.append({'class_date': class_date, 'class_time': class_time})
            stime = time_data.courseid.coursestarttime
            if stime:
                stime = stime.strftime('%Y-%m-%d %X')
            etime = time_data.courseid.courseendtime
            if etime:
                etime = etime.strftime('%Y-%m-%d %X')
            course_type = time_data.courseid.coursetype
            course_type = translateTypeId2Type(course_type)
            data.append({
                'course_id': course_id,
                'course_name': course_name,
                'course_time': course_time,
                'course_start_time': stime,
                'course_end_time': etime,
                'course_type': course_type
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

    return HttpResponse('课表')


def course_select(request):
    """
        课程查看
        @param request:
        @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':

        courses = Course.objects.all()

        data = []
        count = len(courses)

        for each_data in courses:
            course_id = each_data.courseid
            course_type = translateTypeId2Type(each_data.coursetype)
            start_time = each_data.coursestarttime
            end_time = each_data.courseendtime
            register_num = each_data.courseregisternum
            favor_deg = each_data.coursefavordeg
            intro = each_data.courseintro
            state = each_data.coursestate
            name = each_data.coursename
            if start_time:
                start_time = start_time.strftime('%Y-%m-%d %X')

            if end_time:
                end_time = end_time.strftime('%Y-%m-%d %X')
            data.append({
                'course_id': course_id,
                'course_type': course_type,
                'start_time': start_time,
                'end_time': end_time,
                'register_num': str(register_num),
                'favor_deg': str(favor_deg),
                'intro': intro,
                'state': state,
                'name': name,
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


def course_start(request):
    """
    课程开设
    @param request:
    @return:
    """
    # GET请求, 进入课程开设页面
    if request.method == 'GET':
        return render(request, 'temp_课程开设')

    # POST请求, 业务实现
    elif request.method == 'POST':
        # temp_cid = request.POST.get('temp_cid')
        temp_stime = request.POST.get('temp_start_time')
        temp_etime = request.POST.get('temp_end_time')
        temp_type = request.POST.get('temp_type')
        temp_type = translateType2TypeId(temp_type)
        temp_name = request.POST.get('temp_name')
        temp_intro = request.POST.get('temp_intro')
        temp_state = 'reviewing'
        # # 参数不全, 错误
        # if not all([temp_type]):
        #     return HttpResponse('参数不全')

        print(temp_stime)
        print(type(temp_stime))

        course = Course.objects.create(coursestarttime=temp_stime, courseendtime=temp_etime, coursetype=temp_type,
                                       coursename=temp_name, courseintro=temp_intro, coursestate=temp_state)

        coursereview = Coursereview.objects.create(courseid=course, adminid=Admin.objects.order_by('?').first(),
                                                   reviewstate=temp_state)

        # 加入相应表中

        # 返回成功信息。
        return HttpResponse('ok')

    return HttpResponse('开设课程')


def course_change(request):
    """
    课程更改
    @param request:
    @return:
    """
    # GET请求, 进入课程开设页面
    if request.method == 'GET':
        return render(request, 'temp_课程开设')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_cid = request.POST.get('temp_course_id')
        temp_stime = request.POST.get('temp_start_time')
        temp_etime = request.POST.get('temp_end_time')
        temp_type = request.POST.get('temp_type')
        temp_type = translateType2TypeId(temp_type)
        temp_name = request.POST.get('temp_name')
        temp_num = request.POST.get('temp_register_num')
        temp_favor = request.POST.get('temp_favor_degree')
        temp_intro = request.POST.get('temp_intro')

        # 参数不全, 错误
        if not all([temp_cid]):
            return HttpResponse('参数不全')

        # 更改到相应表中
        course = Course.objects.get(courseid=temp_cid)
        if course is not None:
            if temp_stime:
                course.update(coursestarttime=temp_stime)
            if temp_etime:
                course.update(courseendtime=temp_etime)
            if temp_type:
                course.update(coursetype=temp_type)
            if temp_name:
                course.update(cousrename=temp_name)
            if temp_num:
                course.update(courseregisternum=temp_num)
            if temp_favor:
                course.update(coursefavordeg=temp_favor)
            if temp_intro:
                course.update(courseintro=temp_intro)

        # 返回成功信息。
        return HttpResponse('ok')

    return HttpResponse('课程更改')


def course_delete(request):
    """
    课程删除
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':
        temp_cid = request.POST.get('temp_course_id')

        # 参数不全, 错误
        if not all([temp_cid]):
            return HttpResponse('参数不全')
        Course.objects.get(courseid=temp_cid).delete()
        # 返回成功信息。
        return HttpResponse('ok')

    return HttpResponse('删除课程')


def class_start(request):
    """
        课程开设具体的一个班级
        @param request:
        @return:
        """
    # GET请求, 进入课程开设页面
    if request.method == 'GET':
        return render(request, 'temp_课程开设')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_cid = request.POST.get('temp_course_id')
        temp_date = request.POST.get('temp_date')
        temp_date = translateDate2DateId(temp_date)
        temp_time = request.POST.get('temp_time')

        if not any([temp_cid, temp_date, temp_time]):
            return HttpResponse('参数不全')

        course = Course.objects.get(courseid=temp_cid)
        if course:
            if not Class.objects.filter(courseid=temp_cid, classtime=temp_time, classdate=temp_date):
                Class.objects.create(courseid=temp_cid, classtime=temp_time, classdate=temp_date, classstudentnum=0)
                return HttpResponse('ok')
            else:
                return HttpResponse('已存在相应班级')
        else:
            return HttpResponse('不存在该课程')

def class_delete(request):
    """
            删除具体的一个班级
            @param request:
            @return:
            """
    # GET请求, 进入课程开设页面
    if request.method == 'GET':
        return render(request, 'temp_删除班级')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_cid = request.POST.get('temp_class_id')
        # 参数不全, 错误
        if not all([temp_cid]):
            return HttpResponse('参数不全')
        Class.objects.get(classid=temp_cid).delete()
        # 返回成功信息。
        return HttpResponse('ok')

    return HttpResponse('删除班级')


def class_change(request):
    """
    班级更改
    @param request:
    @return:
    """
    # GET请求, 进入课程开设页面
    if request.method == 'GET':
        return render(request, 'temp_班级更改')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_cid = request.POST.get('temp_class_id')
        temp_time = request.POST.get('temp_time')
        temp_date = request.POST.get('temp_date')

        # 参数不全, 错误
        if not all([temp_cid]):
            return HttpResponse('参数不全')

        # 更改到相应表中
        class_ = Class.objects.get(classid=temp_cid)
        if class_ is not None:
            if temp_time:
                class_.update(classtime=temp_time)
            if temp_date:
                class_.update(classdate=translateDate2DateId(temp_date))

        # 返回成功信息。
        return HttpResponse('ok')

    return HttpResponse('班级更改')


def class_select(request):
    """
    班级查看
    @param request:
    @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':

        class_ = Class.objects.all()

        data = []
        count = len(class_)

        for each_data in class_:
            class_id = each_data.classid
            course_id = translateTypeId2Type(each_data.courseid.coursetype)
            student_num = each_data.classstudentnum
            class_date = translateDateId2Date(each_data.classdate)
            class_time = each_data.classtime

            data.append({
                'class_id': class_id,
                'course_id': course_id,
                'student_num': student_num,
                'class_date': class_date,
                'class_time': class_time,
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

    return HttpResponse('班级查看')


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
        temp_cid = request.POST.get('temp_class_id')
        temp_tid = request.POST.get('temp_teacher_id')
        temp_stime = request.POST.get('temp_start_time')
        temp_etime = request.POST.get('temp_end_time')
        temp_content = request.POST.get('temp_content')

        if not all([temp_cid, temp_tid]):
            return HttpResponse('参数不全')

        homework = Homework.objects.create(classid=Class.objects.get(classid=temp_cid),
                                           teacherid=Teacher.objects.get(teacherid=temp_tid),
                                           homeworkstarttime=temp_stime,
                                           homeworkendtime=temp_etime, homeworkcontent=temp_content)
        return HttpResponse('ok')

    return HttpResponse('发布作业')


def homework_change(request):
    """
           作业修改
           @param request:
           @return:
        """
    # GET请求, 进入作业发布页面
    if request.method == 'GET':
        return render(request, 'temp_作业发布')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_hid = request.POST.get('temp_homework_id')

        temp_stime = request.POST.get('temp_start_time')
        temp_etime = request.POST.get('temp_end_time')
        temp_content = request.POST.get('temp_content')

        if not all([temp_hid]):
            return HttpResponse('参数不全')

        # 更改到相应表中
        homework = Homework.objects.filter(homeworkid=temp_hid)

        if homework is not None:
            if temp_stime:
                homework.update(homeworkstarttime=temp_stime)
            if temp_etime:
                homework.update(homeworkendtime=temp_etime)
            if temp_content:
                homework.update(homeworkcontent=temp_content)
            # 返回成功信息。
        return HttpResponse('ok')

    return HttpResponse('课程修改')


def homework_delete(request):
    """
    作业删除
    @param request:
    @return:
    """
    # GET请求, 进入课程删除页面
    if request.method == 'GET':
        return render(request, 'temp_作业删除')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_hid = request.POST.get('temp_homework_id')

        # 参数不全, 错误
        if not all([temp_hid]):
            return HttpResponse('参数不全')
        Homework.objects.get(homeworkid=temp_hid).delete()
        # 返回成功信息。
        return HttpResponse('ok')

    return HttpResponse('删除作业')


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

    # return HttpResponse('预约查询')


def activity_attend(request):
    """
         参加活动
         @param request:
         @return:
    """
    # GET请求, 进入活动参加
    if request.method == 'GET':
        return render(request, 'temp_活动参加')

    # POST请求, 业务实现
    elif request.method == 'POST':
        temp_aid = request.POST.get('temp_activity_id')
        temp_tid = request.POST.get('temp_teacher_id')

        if not all([temp_aid, temp_tid]):
            return HttpResponse('参数不全')
        elif temp_aid and temp_tid:
            attend = Teacherattend.objects.create(activityid=temp_aid, teacherid=temp_tid)
            return HttpResponse('ok')

    return HttpResponse('活动参加')


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
        temp_tid = request.POST.get('temp_activity_id')

        if not all([temp_aid, temp_tid]):
            return HttpResponse('参数不全')
        elif temp_aid and temp_tid:
            Teacherattend.objects.filter(activityid=temp_aid, teacherid=temp_tid).delete()

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
        temp_tid = request.POST.get('temp_teacher_id')

        if temp_aid and temp_tid:
            activities = [Teacherattend.objects.get(activityid=temp_aid, teacherid=temp_tid).activityid]
        elif temp_tid:
            activities = [x.activityid for x in Teacherattend.objects.filter(teacherid=temp_tid)]
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


def student_select(request):
    """
        学生查询
        @param request:
        @return:
    """
    # POST请求, 业务实现
    if request.method == 'POST':

        students = Student.objects.all()

        data = []
        count = len(students)
        for each_data in students:
            student_id = each_data.studentid
            real_name = each_data.realname
            stu_class = Studyingat.objects.filter(studentid=student_id)
            class_id = None
            for stu_class_data in stu_class:
                class_id = stu_class_data.classid.classid

            data.append({
                'student_id': student_id,
                'real_name': real_name,
                'class_id': class_id
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
