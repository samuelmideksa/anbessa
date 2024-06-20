# views.py
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.forms import UserCreationForm, SubscriptionForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from users.models import Subscription
from tickets.models import Ticket
from routes.models import Route


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.user = request.user
            subscription.save()
            return redirect('subscription_success')
    else:
        form = SubscriptionForm()
    return render(request, 'users/subscribe.html', {'form': form})


@login_required
def subscription_success(request):
    return render(request, 'users/subscription_success.html')


@login_required
def subscription_detail(request):
    subscription = get_object_or_404(Subscription, user=request.user)
    return render(request, 'users/subscription_detail.html', {'subscription': subscription})


@login_required
def my_tickets(request):
    tickets = Ticket.objects.filter(user=request.user)
    subscription = Subscription.objects.filter(user=request.user).first()
    return render(request, 'users/my_tickets.html', {'tickets': tickets, 'subscription': subscription})
