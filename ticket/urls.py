# coding=utf-8
from . import views
from django.urls import path

urlpatterns = [
    # path("", views.MyView.as_view()),
    path("add-ticket/", views.AddTicket.as_view()),
    path("list-ticket/", views.ListTicket.as_view(), name="list-ticket"),
    path("update-ticket/<int:pk>", views.UpdateTicket.as_view(), name="update-ticket"),
]