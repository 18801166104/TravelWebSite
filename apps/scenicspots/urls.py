# author wangz
from django.urls import path

from scenicspots.views import ScenicListView, ScenicDetails, ActiveDetails, OrderDetailsView

urlpatterns = [
    path('all/',ScenicListView.as_view(),name='all'),
    # 景点详情
    path('scenic_detail/<int:scenic_id>/', ScenicDetails.as_view(), name='scenic_detail'),
    # 活动详情
    path('active_detail/<int:active_id>/', ActiveDetails.as_view(), name='active_detail'),
    # 旅游订单详情
    path('order_detail/<int:order_num>/',OrderDetailsView.as_view(),name='order_detail'),
]