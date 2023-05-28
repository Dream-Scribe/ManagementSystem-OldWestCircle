from index.models import Student, Teacher


def check_login(phone_number, password, login_type):
    if not all([phone_number, password, login_type]):
        return None

    elif login_type == 'student':
        try:
            student = Student.objects.get(phonenumber=phone_number, userpd=password)
        except Student.DoesNotExist:
            student = None

        if student is not None:
            return 'student'


    elif login_type == 'teacher':
        try:
            teacher = Teacher.objects.get(phonenumber=phone_number, userpd=password)
        except Teacher.DoesNotExist:
            teacher = None

        if teacher is not None:
            return 'teacher'


def check_register(phone_number, password, uuid):
    # 注册成功跳转到到登录页面，注册加判断已经存在提示改用用户已存在
    users = Student.objects.all()
    for i in users:
        if phone_number == i.phonenumber:
            return "用户已存在"
    try:
        Student.objects.create(studentid=uuid, phonenumber=phone_number, userpd=password)
        return "注册成功"
    except Exception as e:
        print(e)
        return "注册失败"

