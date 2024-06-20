from django import forms

from tickets.models import Ticket


class TicketPurchaseForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_type']

