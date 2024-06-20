from django.db import models
from users.models import User
from routes.models import Route


class Ticket(models.Model):
    SINGLE = 'single'
    RETURN = 'return'

    TICKET_TYPE_CHOICES = [
        (SINGLE, 'Single Ticket'),
        (RETURN, 'Return Ticket'),
    ]

    ticket_type = models.CharField(max_length=10, choices=TICKET_TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Ticket for {self.user.username} on route {self.route.origin} to {self.route.destination}"
