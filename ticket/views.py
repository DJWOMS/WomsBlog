from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from django.urls import reverse

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


class ListTicket(ListView):
    """Список тикетов пользователя
    """
    model = Ticket
    # queryset = Ticket.objects.all()
    context_object_name = "tickets"
    template_name = "ticket/list-ticket.html"
    
    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)

 
class UpdateTicket(UpdateView):
    """Редактипрование тикета
    """
    model = Ticket
    form_class = AddTicketForm
    template_name = "ticket/update-ticket.html"

    def get_success_url(self):
        return reverse('list-ticket')
        
    