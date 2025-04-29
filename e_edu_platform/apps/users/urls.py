# -*- codeding = utf-8 -*-
# @Time: 13/09/2021 19:07
# @Author: Changchen
# @File: urls.py
# @Software: PyCharm


from django.conf.urls import url, include

from .views import UserinfoView, UploadImageView, UpdatePwdView #SendEmailCodeView
from .views import UpdateEmailView, MyCourseView, MyFavOrgView, MyFavTeacherView, MyFavCourseView, MymessageView


urlpatterns = [
    #User info
    url('info/', UserinfoView.as_view(), name="user_info"),

    #User img
    url('image/upload/', UploadImageView.as_view(), name="image_upload"),

    #password
    url('update/pwd/', UpdatePwdView.as_view(), name="update_pwd"),

    #code
    #url('sendemail_code/', SendEmailCodeView.as_view(), name="sendemail_code"),

    #email
    url('update_email/', UpdateEmailView.as_view(), name="update_email"),

    #course
    url('mycourse/', MyCourseView.as_view(), name="mycourse"),

    #org
    url('myfav/org/', MyFavOrgView.as_view(), name="myfav_org"),

    #teacher
    url('myfav/teacher/', MyFavTeacherView.as_view(), name="myfav_teacher"),

    #fav_course
    url('myfav/course/', MyFavCourseView.as_view(), name="myfav_course"),

    #message
    url('mymessage/', MymessageView.as_view(), name="mymessage"),
]