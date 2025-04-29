# -*- codeding = utf-8 -*-
# @Time: 08/09/2021 18:59
# @Author: Changchen
# @File: adminx.py
# @Software: PyCharm
import xadmin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'img', 'click_nums',
                    'add_time']  # 展示
    search_fields = ['name', 'desc', 'detail', 'degree', 'students', 'fav_nums', 'img', 'click_nums']  # 搜索框
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'img', 'click_nums',
                   'add_time']  # 筛选


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']  # 展示
    search_fields = ['course', 'name']  # 搜索框
    list_filter = ['course__name', 'name', 'add_time']  # 筛选

class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']  # 展示
    search_fields = ['lesson', 'name']  # 搜索框
    list_filter = ['lesson', 'name', 'add_time']  # 筛选

class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download','add_time']  # 展示
    search_fields = ['course', 'name', 'download']  # 搜索框
    list_filter = ['course', 'name', 'download','add_time']  # 筛选


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)