#_*_ encoding:utf-8 _*_
from django.db import models

from datetime import datetime

from users.models import UserProfile
from courses.models import Course
# Create your models here.

class UserAsk(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"name")
    mobile = models.CharField(max_length=11,verbose_name=u"mobile")
    course_name = models.CharField(max_length=50,verbose_name=u"course_name")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"add_time")

    class Meta:
        verbose_name = u"UserAsk"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    #course comments
    user = models.ForeignKey(UserProfile,verbose_name=u"user",on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name=u"course",on_delete=models.CASCADE)
    comments = models.CharField(max_length=200,verbose_name=u"comments")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"add_time")

    class Meta:
        verbose_name = u"CourseComments"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name=u"user",on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0,verbose_name=u"fav_id")
    fav_type = models.IntegerField(choices=((1,"course"),(2,"organization"),(3,"lecturer")),default=1,verbose_name=u"收藏类型")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"add_time")

    class Meta:
        verbose_name = u"UserFavorite"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name=u"user")
    message = models.CharField(max_length=500,verbose_name=u"message")
    has_read = models.BooleanField(default=False,verbose_name=u"has_read")
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"add_time")

    class Meta:
        verbose_name = u"UserMessage"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name=u"User",on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name=u"Course",on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now,verbose_name=u"Add_time")

    class Meta:
        verbose_name = u"UserCourse"
        verbose_name_plural = verbose_name

