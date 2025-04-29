# -*- codeding = utf-8 -*-
# @Time: 09/09/2021 09:03
# @Author: Changchen
# @File: adminx.py
# @Software: PyCharm

import xadmin
from .models import UserAsk,UserCourse,UserMessage,CourseComments,UserFavorite

class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name','add_time']  # 展示
    search_fields = ['name', 'mobile', 'course_name']  # 搜索框
    list_filter = ['name', 'mobile', 'course_name','add_time']  # 筛选

class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']  # 展示
    search_fields = ['user', 'course']  # 搜索框
    list_filter = ['user', 'course', 'add_time']  # 筛选

class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read','add_time']  # 展示
    search_fields = ['user', 'message', 'has_read']  # 搜索框
    list_filter = ['user', 'message', 'has_read','add_time']  # 筛选

class CourseCommentsAdmin(object):
    list_display = ['user', 'course','comments','add_time']  # 展示
    search_fields = ['user', 'course','comments']  # 搜索框
    list_filter = ['user', 'course','comments','add_time']  # 筛选

class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id','fav_type','add_time']  # 展示
    search_fields = ['user', 'fav_id','fav_type']  # 搜索框
    list_filter = ['user', 'fav_id','fav_type','add_time']  # 筛选

xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
