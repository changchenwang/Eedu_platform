#_*_ encoding:utf-8 _*_
from django.db import models
from datetime import datetime

# Create your models here.
class CityDic(models.Model):
    name = models.CharField(max_length=20,verbose_name=u"name")
    desc = models.TextField(max_length=200,verbose_name=u"desc")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"city"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"CourseOrg")
    desc = models.TextField(verbose_name=u"desc")
    tag = models.CharField(default="tag",max_length=10,verbose_name=u"tag")
    catgory = models.CharField(default="pxjg",verbose_name=u"category",max_length=20,
                               choices=(("pxjg","organization"),
                                        ("gr","personal"),
                                        (("gx","Univercity"))))
    click_nums = models.IntegerField(default=0,verbose_name=u"click_nums")
    fav_nums = models.IntegerField(default=0,verbose_name=u"fav_nums")
    img = models.ImageField(upload_to="org/%Y/%m",verbose_name=u"logo",max_length=100)
    address = models.CharField(max_length=150,verbose_name=u"address")
    city = models.ForeignKey(CityDic,verbose_name=u"city",on_delete=models.CASCADE)
    students = models.IntegerField(default=0,verbose_name=u"students")
    course_nums = models.IntegerField(default=0,verbose_name=u"course_nums")
    add_time = models.DateTimeField(default=datetime.now)
    class Meta:
        verbose_name = u"CourseOrg"
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        #Get the number of teachers in the course institution
        return self.teacher_set.all().count()

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name=u"org",on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name=u"name")
    work_years = models.IntegerField(default=0,verbose_name=u"work_years")
    work_company = models.CharField(max_length=50,verbose_name=u"work_company")
    work_position = models.CharField(max_length=50,verbose_name=u"work_position")
    points = models.CharField(max_length=50,verbose_name=u"points")
    click_nums = models.IntegerField(default=0, verbose_name=u"click_nums")
    fav_nums = models.IntegerField(default=0, verbose_name=u"fav_nums")
    age = models.IntegerField(default=18, verbose_name=u"age")
    img = models.ImageField(default='',upload_to="courses/%Y/%m",verbose_name=u"img",max_length=100)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"teacher"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

