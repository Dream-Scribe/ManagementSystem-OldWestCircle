# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Activity(models.Model):
    activityid = models.BigAutoField(db_column='activityID', primary_key=True)  # Field name made lowercase.
    adminid = models.ForeignKey('Admin', models.DO_NOTHING, db_column='adminID', to_field='adminid')  # Field name made lowercase.
    activitycontent = models.CharField(db_column='activityContent', max_length=100, blank=True, null=True)  # Field name made lowercase.
    activitystarttime = models.DateTimeField(db_column='activityStartTime', blank=True, null=True)  # Field name made lowercase.
    activityendtime = models.DateTimeField(db_column='activityEndTime', blank=True, null=True)  # Field name made lowercase.
    activityplace = models.CharField(db_column='activityPlace', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'activity'


class Admin(models.Model):
    adminid = models.BigIntegerField(db_column='adminID', primary_key=True)  # Field name made lowercase.
    adminpd = models.CharField(db_column='adminPd', max_length=20)  # Field name made lowercase.
    adminname = models.CharField(db_column='adminName', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class Announcement(models.Model):
    announceid = models.BigAutoField(db_column='announceID', primary_key=True)  # Field name made lowercase.
    adminid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminID', to_field='adminid')  # Field name made lowercase.
    announcecontent = models.CharField(db_column='announceContent', max_length=100, blank=True, null=True)  # Field name made lowercase.
    announcepublishtime = models.DateTimeField(db_column='announcePublishTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'announcement'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Booking(models.Model):
    studentid = models.OneToOneField('Student', models.DO_NOTHING, db_column='studentID', primary_key=True)  # Field name made lowercase. The composite primary key (studentID, teacherID, bookTime) found, that is not supported. The first column is selected.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacherID', to_field='teacherid')  # Field name made lowercase.
    booktime = models.DateTimeField(db_column='bookTime')  # Field name made lowercase.
    bookplace = models.CharField(db_column='bookPlace', max_length=30)  # Field name made lowercase.
    bookdescription = models.CharField(db_column='bookDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    booksuccess = models.TextField(db_column='bookSuccess')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'booking'
        unique_together = (('studentid', 'teacherid', 'booktime'),)


class Class(models.Model):
    classid = models.BigAutoField(db_column='classID', primary_key=True)  # Field name made lowercase.
    courseid = models.ForeignKey('Course', models.DO_NOTHING, db_column='courseID', to_field='courseid')  # Field name made lowercase.
    classstudentnum = models.IntegerField(db_column='classStudentNum')  # Field name made lowercase.
    classdate = models.IntegerField(db_column='classDate', blank=True, null=True)  # Field name made lowercase.
    classtime = models.CharField(db_column='classTime', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'class'


class Course(models.Model):
    courseid = models.BigAutoField(db_column='courseID', primary_key=True)  # Field name made lowercase.
    coursetype = models.IntegerField(db_column='courseType')  # Field name made lowercase.
    coursestarttime = models.DateTimeField(db_column='courseStartTime', blank=True, null=True)  # Field name made lowercase.
    courseendtime = models.DateTimeField(db_column='courseEndTime', blank=True, null=True)  # Field name made lowercase.
    courseregisternum = models.IntegerField(db_column='courseRegisterNum', blank=True, null=True)  # Field name made lowercase.
    coursefavordeg = models.DecimalField(db_column='courseFavorDeg', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    courseintro = models.CharField(db_column='courseIntro', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coursestate = models.CharField(db_column='courseState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    coursename = models.CharField(db_column='courseName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'


class Coursereview(models.Model):
    courseid = models.OneToOneField(Course, models.DO_NOTHING, db_column='courseID', primary_key=True)  # Field name made lowercase.
    adminid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminID', to_field='adminid')  # Field name made lowercase.
    reviewreason = models.CharField(db_column='reviewReason', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reviewstate = models.CharField(db_column='reviewState', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coursereview'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Homework(models.Model):
    homeworkid = models.BigAutoField(db_column='homeworkID', primary_key=True)  # Field name made lowercase.
    classid = models.ForeignKey(Class, models.DO_NOTHING, db_column='classID', to_field='classid')  # Field name made lowercase.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacherID', to_field='teacherid')  # Field name made lowercase.
    homeworkstarttime = models.DateTimeField(db_column='homeworkStartTime')  # Field name made lowercase.
    homeworkendtime = models.DateTimeField(db_column='homeworkEndTime')  # Field name made lowercase.
    homeworkcontent = models.CharField(db_column='homeworkContent', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'homework'


class Student(models.Model):
    studentid = models.BigIntegerField(db_column='studentID', primary_key=True)  # Field name made lowercase.
    registertime = models.DateTimeField(db_column='registerTime', blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='nickName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    realname = models.CharField(db_column='realName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=15)  # Field name made lowercase.
    userpd = models.CharField(db_column='userPD', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class Studentattend(models.Model):
    activityid = models.OneToOneField(Activity, models.DO_NOTHING, db_column='activityID', primary_key=True)  # Field name made lowercase. The composite primary key (activityID, studentID) found, that is not supported. The first column is selected.
    studentid = models.ForeignKey(Student, models.DO_NOTHING, db_column='studentID', to_field='studentid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studentattend'
        unique_together = (('activityid', 'studentid'),)


class Studenttocoursecomment(models.Model):
    studentid = models.OneToOneField(Student, models.DO_NOTHING, db_column='studentID', primary_key=True)  # Field name made lowercase. The composite primary key (studentID, courseID) found, that is not supported. The first column is selected.
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseID', to_field='courseid')  # Field name made lowercase.
    s2cstar = models.IntegerField(db_column='s2cStar', blank=True, null=True)  # Field name made lowercase.
    s2ccomment = models.CharField(db_column='s2cComment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    s2ccommenttime = models.DateTimeField(db_column='s2cCommentTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studenttocoursecomment'
        unique_together = (('studentid', 'courseid'),)


class Studenttoteachercomment(models.Model):
    studentid = models.OneToOneField(Student, models.DO_NOTHING, db_column='studentID', primary_key=True)  # Field name made lowercase. The composite primary key (studentID, teacherID) found, that is not supported. The first column is selected.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacherID', to_field='teacherid')  # Field name made lowercase.
    s2tstar = models.IntegerField(db_column='s2tStar')  # Field name made lowercase.
    s2tcomment = models.CharField(db_column='s2tComment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    s2tcommenttime = models.DateTimeField(db_column='s2tCommentTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studenttoteachercomment'
        unique_together = (('studentid', 'teacherid'),)


class Studyingat(models.Model):
    studentid = models.OneToOneField(Student, models.DO_NOTHING, db_column='studentID', primary_key=True)  # Field name made lowercase. The composite primary key (studentID, classID) found, that is not supported. The first column is selected.
    classid = models.ForeignKey(Class, models.DO_NOTHING, db_column='classID', to_field='classid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studyingat'
        unique_together = (('studentid', 'classid'),)


class Teach(models.Model):
    teacherid = models.OneToOneField('Teacher', models.DO_NOTHING, db_column='teacherID', primary_key=True)  # Field name made lowercase. The composite primary key (teacherID, courseID) found, that is not supported. The first column is selected.
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseID', to_field='courseid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teach'
        unique_together = (('teacherid', 'courseid'),)


class Teacher(models.Model):
    teacherid = models.BigIntegerField(db_column='teacherID', primary_key=True)  # Field name made lowercase.
    registertime = models.DateTimeField(db_column='registerTime', blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='nickName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    realname = models.CharField(db_column='realName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=15)  # Field name made lowercase.
    userpd = models.CharField(db_column='userPD', max_length=20)  # Field name made lowercase.
    teacherintro = models.CharField(db_column='teacherIntro', max_length=100, blank=True, null=True)  # Field name made lowercase.
    teacherfield = models.IntegerField(db_column='teacherField')  # Field name made lowercase.
    teacherwelcomedeg = models.DecimalField(db_column='teacherWelcomeDeg', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    teacherclasshour = models.IntegerField(db_column='teacherClassHour', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teacher'


class Teacherattend(models.Model):
    activityid = models.OneToOneField(Activity, models.DO_NOTHING, db_column='activityID', primary_key=True)  # Field name made lowercase. The composite primary key (activityID, teacherID) found, that is not supported. The first column is selected.
    teacherid = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='teacherID', to_field='teacherid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teacherattend'
        unique_together = (('activityid', 'teacherid'),)


class Teachertostudentcomment(models.Model):
    studentid = models.OneToOneField(Student, models.DO_NOTHING, db_column='studentID', primary_key=True)  # Field name made lowercase. The composite primary key (studentID, teacherID) found, that is not supported. The first column is selected.
    teacherid = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='teacherID', to_field='teacherid')  # Field name made lowercase.
    t2sstar = models.IntegerField(db_column='t2sStar')  # Field name made lowercase.
    t2scomment = models.CharField(db_column='t2sComment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t2scommenttime = models.DateTimeField(db_column='t2sCommentTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teachertostudentcomment'
        unique_together = (('studentid', 'teacherid'),)
