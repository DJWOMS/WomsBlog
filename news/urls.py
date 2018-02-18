# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name="list_news"),
    path('single/<int:pk>', views.new_single, name="new_single"),
    path('filter/<int:pk>', views.news_filter, name="news_filter"),
]
