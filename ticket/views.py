from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .models import Ticket
from .forms import AddTicketForm


class AddTicket(CreateView):
    """ Добавление тикета
    """
    model = Ticket
    form_class = AddTicketForm
    template_name = "ticket/add-ticket.html"
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect("/ticket/add-ticket/")
    
        
    def success_url(self):
        return redirect("/add-ticket/")
