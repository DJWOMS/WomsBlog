from django.contrib import admin
from .models import Ticket, CategoryTicket

admin.site.register(Ticket)
admin.site.register(CategoryTicket)