from django.urls import path
from tickets import views as tickets_views

urlpatterns = [
    path('tickets/purchase/<int:route_id>/', tickets_views.purchase_ticket, name='purchase_ticket'),
    path('tickets/<int:ticket_id>/', tickets_views.ticket_detail, name='ticket_detail'),
    ]
