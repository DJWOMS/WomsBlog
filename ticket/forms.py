# coding=utf-8
from django import forms
from .models import Ticket


class AddTicketForm(forms.ModelForm):
    """ Форма добавления тикетов
    """
    class Meta:
        model = Ticket
        fields = ("category", "title", "text")
