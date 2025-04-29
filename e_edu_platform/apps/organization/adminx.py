# -*- codeding = utf-8 -*-
# @Time: 09/09/2021 08:47
# @Author: Changchen
# @File: adminx.py
# @Software: PyCharm
import xadmin

from .models import CityDic, CourseOrg, Teacher

class CityDicAdmin(object):
    list_display = ['name', 'desc', 'add_time']  # 展示
    search_fields = ['name', 'desc']  # 搜索框
    list_filter = ['name', 'desc', 'add_time']  # 筛选

class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums','fav_nums','img','address','city']  # 展示
    search_fields = ['name', 'desc', 'click_nums','fav_nums','img','address','city']  # 搜索框
    list_filter = ['name', 'desc', 'click_nums','fav_nums','img','address','city']  # 筛选

class TeacherAdmin(object):
    list_display = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums','add_time']  # 展示
    search_fields = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums']
    list_filter = ['org','name','work_years','work_company','work_position','points','click_nums','fav_nums','add_time']   # 筛选



xadmin.site.register(CityDic, CityDicAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)