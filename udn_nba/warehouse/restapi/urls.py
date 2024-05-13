from django.urls import path
from . import api

urlpatterns = [
    path('', api.news_list, name='news-list'),
    path('content/<int:id>', api.news_detail, name='news-detail'),
]