"""TravelWebSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import DjangoUeditor
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.static import serve


from TravelWebSite.settings import MEDIA_ROOT,STATICFILES_DIRS
from users.views import *
from users import views
urlpatterns = [
    # 工具
    path('admin/', admin.site.urls),
    re_path(r'^captcha/', include('captcha.urls')),
    # 网站页面
    # 首页
    path('index/',IndexView.as_view(),name='index'),
    # 新闻资讯
    path('news/',include(('news.urls','news'))),
    # 旅游页面
    path('scenicspots/', include(('scenicspots.urls', 'scenicspots')), name='scenicspots'),
    # 商城相关
    path('shop/', include(('shop.urls', 'shop')), name='shop'),
    # 游记相关
    path('diarys/', include(('diarys.urls', 'diarys')), name='diarys'),

    # 用户相关
    # 注册
    path('register/',RegisterView.as_view(),name='register'),
    # 登陆
    path('login/',LoginView.as_view(),name='login'),
    # 登出
    path('logout/',LogoutView.as_view(),name='logout'),
    # 签到页面
    path('check/', CheckView.as_view(), name='check'),
    # 设置页面
    path('userinfo/<slug:info_type>', UserInfoView.as_view(), name='userinfo'),
    # 用户上传路径 访问上传图片的路径
    re_path(r'media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    # 我的收藏
    path('mycollect', MyCollectView.as_view(), name='mycollect'),
    # 我的评论
    path('mycomments', MyCommentsView.as_view(), name='mycomments'),
    # 我的主页
    # path('homepage', login_required(HomePageView.as_view()), name='homepage'),
    path('homepage', HomePageView.as_view(), name='homepage'),
    # 其余操作相关
    path('operation/', include(('operation.urls', 'operation')), name='operation'),

    # 支付相关
    path('pay/', include(('pay.urls', 'pay')), name='pay'),
    path('indextest',views.indexTest),
    # static文件路径
    # re_path(r'sAtaticS/(?P<path>.*)$',serve,{"document_root": STATICFILES_DIRS}),
        re_path(r'^ueditor/',include('DjangoUeditor.urls'))
]
