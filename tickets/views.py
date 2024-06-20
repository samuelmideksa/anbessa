# views.py
from django.shortcuts import render, redirect, get_object_or_404

from users.models import Subscription
from .models import Ticket, Route
from .forms import TicketPurchaseForm
from django.contrib.auth.decorators import login_required


@login_required
def purchase_ticket(request, route_id):
    route = get_object_or_404(Route, id=route_id)

    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.route = route
            ticket.price = calculate_ticket_price(ticket.ticket_type)
            ticket.save()
            return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        form = TicketPurchaseForm()

    return render(request, 'tickets/purchase_ticket.html', {'form': form, 'route': route})


@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})


def calculate_ticket_price(ticket_type):
    # Implement the logic to calculate the price based on the tickets type
    if ticket_type == 'single':
        return 2.50
    elif ticket_type == 'return':
        return 4.00
    elif ticket_type == 'pass':
        return 30.00
    else:
        return 0
