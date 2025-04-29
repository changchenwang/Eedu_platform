# -*- codeding = utf-8 -*-
# @Time: 13/09/2021 16:00
# @Author: Changchen
# @File: urls.py
# @Software: PyCharm


from django.conf.urls import url, include

from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView
from .views import TeacherListView, TeacherDetailView

app_name ='[org]'
urlpatterns = [
    #Organization list
    url('list/', OrgView.as_view(), name="org_list"),
    url('add_ask/', AddUserAskView.as_view(), name="add_ask"),
    url('home/(?P<org_id>\d+)/', OrgHomeView.as_view(), name="org_home"),
    url('course/(?P<org_id>\d+)/', OrgCourseView.as_view(), name="org_course"),
    url('desc/(?P<org_id>\d+)/', OrgDescView.as_view(), name="org_desc"),
    url('org_teacher/(?P<org_id>\d+)/', OrgTeacherView.as_view(), name="org_teacher"),

    #favorite org
    url('add_fav/', AddFavView.as_view(), name="add_fav"),

    #teacher list
    url('teacher/list/', TeacherListView.as_view(), name="teacher_list"),

    #teacher detail
    url('teacher/detail/(?P<teacher_id>\d+)/', TeacherDetailView.as_view(), name="teacher_detail"),


]