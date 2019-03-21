# author wangz
from django.urls import path

from diarys.views import AllDiaryView, GetdiarayView, MyDetailsView, DetailsView, SetdiarayView

urlpatterns = [
    path('all/<slug:diary_type>/', AllDiaryView.as_view(), name='all'),
    path('getdiaray/<int:diary_id>',GetdiarayView.as_view(),name='getdiaray'),
    path('mydetails/<slug:is_published>',MyDetailsView.as_view(),name='mydetails'),
    # 修改游记
    path('setdiaray/<slug:operation_type>/<int:diary_id>',SetdiarayView.as_view(),name='setdiaray'),
    # 游记详情
    path('details/<int:diary_id>/', DetailsView.as_view(), name='details'),
]