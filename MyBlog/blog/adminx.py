# -*-coding:utf-8-*-

__Author__ = "Mr.D"
__Date__ = '2018\4\10 0010 15:46'


import xadmin
from xadmin import views
from .models import UserProfile, LearnProfile, LifeProfile, AboutMe


class BaseSetting(object):
    enable_theMes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "蓝鲤歌蓝的博客"
    site_footer = "蓝鲤歌蓝"
    menu_style = 'accordion'


class UserProfileAdimin(object):
    list_display = ('title', 'pub')
    search_fields = ['title', 'pub']
    list_filter = ['title', 'pub']


class LearnProfileAdmin(object):
    search_fields = ['title', 'pub']
    list_display = ('title', 'pub')
    list_filter = ['title', 'pub']


class LifeProfileAdmin(object):
    list_display = ('title', 'pub')
    search_fields = ['title', 'pub']
    list_filter = ['title', 'pub']


class AboutMeAdmin(object):
    list_display = ('content',)
    search_fields = ['content']
    list_filter = ['content']


xadmin.site.register(UserProfile, UserProfileAdimin)
xadmin.site.register(LearnProfile, LearnProfileAdmin)
xadmin.site.register(LifeProfile, LifeProfileAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(AboutMe, AboutMeAdmin)
