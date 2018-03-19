# coding=utf-8
from . import views
from django.urls import path

urlpatterns = [
    # path("", views.MyView.as_view()),
    path("add-ticket/", views.AddTicket.as_view())
]