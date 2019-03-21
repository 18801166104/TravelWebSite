from django.urls import path
from news import views



urlpatterns = [
    path('all/',views.NewsView.as_view(),name='all'),
    path('detail/<int:news_id>',views.NewsDetails.as_view(),name='news_detail')
]