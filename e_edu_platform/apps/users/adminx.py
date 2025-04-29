# -*- codeding = utf-8 -*-
# @Time: 08/09/2021 15:54
# @Author: Changchen
# @File: adminx.py
# @Software: PyCharm
import xadmin
from xadmin import views
from .models import Banner

#全局配置
class BaseSetting(object):
    enable_themes = True #主题功能
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "Changchen Mooc"
    site_footer = "Changchen"
    menu_style = "accordion" #把app折叠起来


class EmailVarifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time'] #邮箱验证码展示
    search_fields = ['code','email','send_type'] #搜索框 搜索验证码
    list_filter = ['code','email','send_type','send_time'] #筛选

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time']  # 邮箱验证码展示
    search_fields = ['title', 'image', 'url', 'index'] # 搜索框 搜索验证码
    list_filter = ['title', 'image', 'url', 'index','add_time']  # 筛选

#xadmin.site.register(EmailVerifyRecord, EmailVarifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin) #model和admin链接
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)