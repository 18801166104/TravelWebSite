import json

from captcha.helpers import captcha_image_url
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
# Create your views here.
from pay.models import OrderItems
from .forms import *

from captcha.models import CaptchaStore
from .models import *
from news.models import *
from scenicspots.models import Active,Spots
from shop.models import Product
from diarys.models import Diary
class IndexView(View):
    '''
    首页
    '''
    def get(self, request):
        # banner
        banners = Banner.objects.all()

        # 精彩活动
        actives = Active.objects.order_by('-add_time')[:3]
        # 热门景区
        natural_spots = Spots.objects.filter(classification='natural')
        # 休闲度假
        leisure_spots = Spots.objects.filter(classification='leisure')
        # 特产商城
        products = Product.objects.order_by('-buyers')[:5]
        # 游记文章
        diarys = Diary.objects.order_by('-praisenum')[:4]
        # 活动资讯
        active_news = News.objects.filter(classification='active')[:4]
        # 热点资讯
        hot_news = News.objects.filter(classification='hot')[:3]
        # 最新资讯
        news = News.objects.order_by('-add_time')[:6]

        return render(request, 'index.html', {
            'now_type': 'index',
            'banners': banners,
            'actives': actives,
            'natural_spots': natural_spots,
            'leisure_spots': leisure_spots,
            'products': products,
            'diarys': diarys,
            'active_news': active_news,
            'hot_news': hot_news,
            'news': news,
        })


class RegisterView(View):
    '''
    注册
    '''

    def get(self, request):
        register_form = RegisterForm()
        hashkey = CaptchaStore.generate_key()
        image_url = captcha_image_url(hashkey)
        return render(request, 'register.html',
                      {'register_form': register_form, 'hashkey': hashkey, 'image_url': image_url, })

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # user_name = request.POST.get('email','')
            user_name = register_form.cleaned_data['email']
            if MyUser.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '用户已经存在'})
            password = request.POST.get('password', '')
            user_profile = MyUser()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(password)
            # user_profile.save()
            user = MyUser.objects.create_user(username=user_name,password=password,email=user_name,is_active=False)
            user.save()
            messages.add_message(request, messages.SUCCESS, '注册成功！请在邮箱中点击激活链接激活账号！')
            return render(request, 'register.html', {})
        else:
            hashkey = CaptchaStore.generate_key()
            image_url = captcha_image_url(hashkey)
            return render(request, 'register.html',
                          {'register_form': register_form, 'hashkey': hashkey, 'image_url': image_url, })


class LoginView(View):
    def get(self, request):
        next = request.GET.get('next','')
        login_form = LoginForm()
        return render(request, 'login.html', {'login_form':login_form,'next':next})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            is_keep = request.POST.get('is_keep', '')
            next = request.POST.get('next','')
            user = authenticate(username=username, password=password)
            # user = MyUser.objects.get(username = username)
            # pwd = user.password
            # if check_password(password,pwd):
            # 如果用户存在
            if user is not None:
                login(request, user)
                if not is_keep:
                    # 关闭浏览器session实效
                    request.session.set_expiry(0)
                if next:
                    return HttpResponseRedirect(next)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {'login_form': login_form,'msg': '用户名或密码错误！'})
        else:
            return render(request, 'login.html', {'login_form': login_form})

class LogoutView(View):
    """
    退出
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

class CheckView(View):
    """
    签到
    """
    def post(self, request):
        username = request.POST['user']
        user = MyUser.objects.filter(username=username)
        now = datetime.now().strftime('%Y-%m-%d')
        for now_user in user:
            if str(now_user.check_time) != now:
                now_user.integral += 20
                now_user.check_time = now
                now_user.save()
                result = json.dumps({"status":"success", "msg":"签到成功"}, ensure_ascii=False)
            else:
                result = json.dumps({"status": "fail", "msg": "签到失败，今天已经签过了"}, ensure_ascii=False)
            return HttpResponse(result)


def log_require(func):
    def inner(home,request):

        if request.user.is_authenticated:
            print(request.user)
            return func(home,request)
        else:
            print('去登陆')
            return render(request,'login.html',{})
    return inner
# 登陆检查两种方式 一 在方法上添加login_required装饰器 默认login_url accounts/login ,可以
# 在settings设置自己的loginurl，为了跳转需要传递next参数，修改login.html
# 二 基于类的视图 需要继承  LoginRequiredMixin
@login_required(login_url='login?next=/indextest')
def indexTest(request):
    banners = Banner.objects.all()

    # 精彩活动
    actives = Active.objects.order_by('-add_time')[:3]
    # 热门景区
    natural_spots = Spots.objects.filter(classification='natural')
    # 休闲度假
    leisure_spots = Spots.objects.filter(classification='leisure')
    # 特产商城
    products = Product.objects.order_by('-buyers')[:5]
    # 游记文章
    diarys = Diary.objects.order_by('-praisenum')[:4]
    # 活动资讯
    active_news = News.objects.filter(classification='active')[:4]
    # 热点资讯
    hot_news = News.objects.filter(classification='hot')[:3]
    # 最新资讯
    news = News.objects.order_by('-add_time')[:6]

    return render(request, 'index.html',
                  {'now_type': 'index', 'banners': banners, 'actives': actives, 'natural_spots': natural_spots,
                      'leisure_spots': leisure_spots, 'products': products, 'diarys': diarys,
                      'active_news': active_news, 'hot_news': hot_news, 'news': news, })

class HomePageView(LoginRequiredMixin,View):
    # @login_required
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(*args,**kwargs)
    def get(self, request):
        user = request.user
        # 游记评论
        diary_comments = user.diarycomments_set.all().order_by('-add_time')
        # 景点评论
        spots_comments = user.spotscomments_set.all().order_by('-add_time')
        # 活动评论
        actives_comments = user.activecomments_set.all().order_by('-add_time')
        # 商品评论
        project_comments = user.productcomments_set.all().order_by('-add_time')
        # 我的游记[已发表]
        diarys = user.diary_set.all().order_by('-add_times').filter(is_published=True)
        # 我的收藏
        collects = user.usercollect_set.all().order_by('-add_time')
        # 旅游订单
        scenic_orders = user.scenicordersmaintable_set.all().order_by('-create_time')
        # 商品订单
        pro_orders = user.goodsordersmaintable_set.all().order_by('-create_time')

        # 获取订单号对应的详细信息
        project_orders = []
        for orders in pro_orders[:5]:
            orders_dic = {}
            # 订单号
            orders_dic['order_num'] = orders.order_num
            # 下单日期
            orders_dic['create_time'] = orders.create_time
            # 总价
            orders_dic['totalprice'] = orders.total_amount
            # 订单状态
            orders_dic['order_state'] = orders.order_state

            goods_list = []
            goods = OrderItems.objects.filter(order_num=orders_dic['order_num'])
            for good in goods:
                goods_dic = {}
                # 商品名
                goods_dic['good_name'] = good.good_name
                # 商品数量
                goods_dic['good_num'] = good.good_num
                # 商品单价
                goods_dic['good_price'] = good.good_price
                # 商品图片
                goods_dic['good_image'] = good.good_image
                # 商品id
                goods_dic['good_id'] = good.good_id

                goods_list.append(goods_dic)

            orders_dic['goods_list'] = goods_list

            project_orders.append(orders_dic)

        return render(request, 'my_index.html', {
            'diary_comments': diary_comments[:5],
            'diary_comments_count': diary_comments.count(),
            'spots_comments': spots_comments[:5],
            'spots_comments_count': spots_comments.count(),
            'actives_comments': actives_comments[:5],
            'actives_comments_count': actives_comments.count(),
            'project_comments': project_comments[:5],
            'project_comments_count': project_comments.count(),
            'diarys': diarys[:3],
            'diarys_count': diarys.count(),
            'collects': collects[:3],
            'collects_count': collects.count(),
            'scenic_orders': scenic_orders[:5],
            'scenic_orders_count': scenic_orders.count(),
            'project_orders': project_orders,
            'project_orders_count': pro_orders.count(),
        })

class UserInfoView(View):
    def get(self,request):
        return render(request,'my_info.html',{})

class MyCollectView(View):
    def get(self,request):
        return render(request,'collection_list.html',{})


class MyCommentsView(View):
    """
    我的评论
    """
    def get(self,request):
        render(request,'my_comments.html',{})