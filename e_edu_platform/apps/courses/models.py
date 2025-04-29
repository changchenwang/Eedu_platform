from django.utils import timezone
from django.db import models

from organization.models import CourseOrg, Teacher

# Create your models here.

class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg,verbose_name=u"organizatio",null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,verbose_name=u"Course name")
    desc = models.CharField(max_length=300,verbose_name=u"Course description")
    detail = models.TextField(verbose_name=u"Course details")
    teacher = models.ForeignKey(Teacher,verbose_name=u"lecturer",null=True,blank=True,on_delete=models.CASCADE)
    is_banner = models.BooleanField(default=False, verbose_name=u"is banner")
    degree = models.CharField(choices=(("cj","primary"),("zj","intermediate"),("gj","senior")),max_length=2,verbose_name=u"difficult")
    learn_times = models.IntegerField(default=0,verbose_name=u"Learning Duration(minutes)")
    students = models.IntegerField(default=0,verbose_name=u"The number of learning")
    fav_nums = models.IntegerField(default=0,verbose_name=u"The number of collection")
    img = models.ImageField(upload_to="courses/%Y/%m",verbose_name=u"cover",max_length=100)
    click_nums = models.IntegerField(default=0,verbose_name=u"clicks")
    category = models.CharField(default=u"The backend development",max_length=300,verbose_name=u"Course category")
    tag = models.CharField(default="",verbose_name=u"Class label",max_length=10)
    youneed_know = models.CharField(default="",max_length=300,verbose_name=u"Course information")
    teacher_tell = models.CharField(default="",max_length=300,verbose_name=u"The teacher tells you")
    add_time = models.DateTimeField(default=timezone.now,verbose_name=u"Add Time")

    class Meta:
        verbose_name = u"Course"
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        #Gets the number of course chapters
        return self.lesson_set.all().count()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        #Get all sections of the course
        return self.lesson_set.all()

    def __unicode__(self):  #错误的
        return self.name

class Lesson(models.Model):
    course = models.ForeignKey(Course,verbose_name=u"Course",on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name=u"Chapter")
    add_time = models.DateTimeField(default=timezone.now,verbose_name=u"Add time")

    class Meta:
        verbose_name = u"Chapter"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_lesson_video(self):
        #Get chapter video
        return self.video_set.all()

class Video(models.Model):
    lesson = models.ForeignKey(Lesson,verbose_name=u"Lesson",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"name")
    learn_times = models.IntegerField(default=0,verbose_name=u"Learning Duration(minutes)")
    url = models.CharField(max_length=200,default="",verbose_name=u"Access to the address")
    add_time = models.DateTimeField(default=timezone.now, verbose_name=u"Add the time")

    class Meta:
        verbose_name = u"video"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"Course",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"name")
    download = models.FileField(upload_to="course/resouce/%Y/%m",verbose_name=u"Resource file",max_length=100)
    add_time = models.DateTimeField(default=timezone.now, verbose_name=u"add time")

    class Meta:
        verbose_name = u"resource file"
        verbose_name_plural = verbose_name