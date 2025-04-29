"""online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

import users
from users.views import LogoutView,LoginView,RegisterView,AciveUserView,ResetView
from organization.views import OrgView
from users.views import IndexView
#ForgetPwdView
from online.settings import MEDIA_ROOT


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('',IndexView.as_view(),name="index"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/',RegisterView.as_view(),name="register"),
    path('active/(?P<active_code>\.*)/,',AciveUserView.as_view(), name="user_active"),
    #path('forget/',ForgetPwdView.as_view(), name="forget_pwd"), 没做出来
    #path('captcha/', include('captcha.urls')),
    path('reset/(?P<active_code>.*)/', ResetView.as_view(), name="reset_pwd"),

#课程机构url配置
    path('org/', include(('organization.urls','organization'), namespace="org")),

#配置上传文件的访问处理函数
    # path('media/(?P<path>.*)',  serve, {"document_root":MEDIA_ROOT}),
    #path('static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),

    #课程相关url配置
    path('course/', include(('courses.urls','courses'), namespace = 'course')),


#课程相关url配置
    path('users/', include(("users.urls","users"),namespace="users")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'