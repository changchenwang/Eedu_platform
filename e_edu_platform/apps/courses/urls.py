# -*- codeding = utf-8 -*-
# @Time: 14/09/2021 10:45
# @Author: Changchen
# @File: urls.py
# @Software: PyCharm

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddComentsView

urlpatterns = [
    #list
    url('list/', CourseListView.as_view(), name="course_list"),

    #detail
    url('detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name="course_detail"),

    url('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name="course_info"),

    #comment
    url('comment/(?P<course_id>\d+)/', CommentsView.as_view(), name="course_comments"),

    #add comment
    url('add_comment/', AddComentsView.as_view(), name="add_comment"),

    # url('video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name="video_play"),

]