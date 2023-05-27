# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activity(models.Model):
    activityid = models.BigIntegerField(db_column='activityID', primary_key=True)  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'admin'


class Announcement(models.Model):
    announceid = models.BigIntegerField(db_column='announceID', primary_key=True)  # Field name made lowercase.
    adminid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminID', to_field='adminid')  # Field name made lowercase.
    announcecontent = models.CharField(db_column='announceContent', max_length=100, blank=True, null=True)  # Field name made lowercase.
    announcepublishtime = models.DateTimeField(db_column='announcePublishTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'announcement'


class Attend(models.Model):
    activityid = models.OneToOneField(Activity, models.DO_NOTHING, db_column='activityID', primary_key=True)  # Field name made lowercase. The composite primary key (activityID, userID) found, that is not supported. The first column is selected.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', to_field='userid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attend'
        unique_together = (('activityid', 'userid'),)


class Booking(models.Model):
    studentid = models.OneToOneField('Student', models.DO_NOTHING, db_column='studentID', primary_key=True)  # Field name made lowercase. The composite primary key (studentID, teacherID, bookTime) found, that is not supported. The first column is selected.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacherID', to_field='userid')  # Field name made lowercase.
    booktime = models.DateTimeField(db_column='bookTime')  # Field name made lowercase.
    bookplace = models.CharField(db_column='bookPlace', max_length=30)  # Field name made lowercase.
    bookdescription = models.CharField(db_column='bookDescription', max_length=100, blank=True, null=True)  # Field name made lowercase.
    booksuccess = models.IntegerField(db_column='bookSuccess')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking'
        unique_together = (('studentid', 'teacherid', 'booktime'),)


class Class(models.Model):
    classid = models.BigIntegerField(db_column='classID', primary_key=True)  # Field name made lowercase.
    courseid = models.ForeignKey('Course', models.DO_NOTHING, db_column='courseID', to_field='courseid')  # Field name made lowercase.
    classstudentnum = models.IntegerField(db_column='classStudentNum')  # Field name made lowercase.
    classtime = models.IntegerField(db_column='classTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'class'


class Course(models.Model):
    courseid = models.BigIntegerField(db_column='courseID', primary_key=True)  # Field name made lowercase.
    coursetype = models.IntegerField(db_column='courseType')  # Field name made lowercase.
    coursestarttime = models.DateTimeField(db_column='courseStartTime', blank=True, null=True)  # Field name made lowercase.
    courseendtime = models.DateTimeField(db_column='courseEndTime', blank=True, null=True)  # Field name made lowercase.
    courseregisternum = models.IntegerField(db_column='courseRegisterNum', blank=True, null=True)  # Field name made lowercase.
    coursefavordeg = models.DecimalField(db_column='courseFavorDeg', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    courseintro = models.CharField(db_column='courseIntro', max_length=100, blank=True, null=True)  # Field name made lowercase.
    coursestate = models.CharField(db_column='courseState', max_length=10, blank=True, null=True)  # Field name made lowercase.

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


class Homework(models.Model):
    homeworkid = models.BigIntegerField(db_column='homeworkID', primary_key=True)  # Field name made lowercase.
    classid = models.ForeignKey(Class, models.DO_NOTHING, db_column='classID', to_field='classid')  # Field name made lowercase.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacherID', to_field='userid')  # Field name made lowercase.
    homeworkstarttime = models.DateTimeField(db_column='homeworkStartTime')  # Field name made lowercase.
    homeworkendtime = models.DateTimeField(db_column='homeworkEndTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'homework'


class Student(models.Model):
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='userID', primary_key=True)  # Field name made lowercase.
    registertime = models.DateTimeField(db_column='registerTime', blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='nickName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    realname = models.CharField(db_column='realName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=15)  # Field name made lowercase.
    userpd = models.CharField(db_column='userPD', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'


class Studenttocoursecomment(models.Model):
    userid = models.OneToOneField(Student, models.DO_NOTHING, db_column='userID', primary_key=True)  # Field name made lowercase. The composite primary key (userID, courseID) found, that is not supported. The first column is selected.
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseID', to_field='courseid')  # Field name made lowercase.
    s2cstar = models.IntegerField(db_column='s2cStar', blank=True, null=True)  # Field name made lowercase.
    s2ccomment = models.CharField(db_column='s2cComment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    s2ccommenttime = models.DateTimeField(db_column='s2cCommentTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studenttocoursecomment'
        unique_together = (('userid', 'courseid'),)


class Studenttoteachercomment(models.Model):
    studentid = models.BigIntegerField(db_column='studentID', primary_key=True)  # Field name made lowercase. The composite primary key (studentID, teacherID) found, that is not supported. The first column is selected.
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacherID', to_field='userid')  # Field name made lowercase.
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
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='userID', primary_key=True)  # Field name made lowercase.
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


class Teachertostudentcomment(models.Model):
    studentid = models.OneToOneField(Student, models.DO_NOTHING, db_column='studentID', primary_key=True)  # Field name made lowercase. The composite primary key (studentID, teacherID) found, that is not supported. The first column is selected.
    teacherid = models.ForeignKey(Teacher, models.DO_NOTHING, db_column='teacherID', to_field='userid')  # Field name made lowercase.
    t2sstar = models.IntegerField(db_column='t2sStar')  # Field name made lowercase.
    t2scomment = models.CharField(db_column='t2sComment', max_length=100, blank=True, null=True)  # Field name made lowercase.
    t2scommenttime = models.DateTimeField(db_column='t2sCommentTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'teachertostudentcomment'
        unique_together = (('studentid', 'teacherid'),)


class User(models.Model):
    userid = models.BigIntegerField(db_column='userID', primary_key=True)  # Field name made lowercase.
    registertime = models.DateTimeField(db_column='registerTime', blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(db_column='nickName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    realname = models.CharField(db_column='realName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=15)  # Field name made lowercase.
    userpd = models.CharField(db_column='userPD', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
