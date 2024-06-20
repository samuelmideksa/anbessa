from django.urls import path, include
from users import views as users_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', users_views.SignUpView.as_view(), name='signup'),
    path('subscribe/', users_views.subscribe, name='subscribe'),
    path('subscription_success/', users_views.subscription_success, name='subscription_success'),
    path('subscription/', users_views.subscription_detail, name='subscription_detail'),
    path('my_tickets/', users_views.my_tickets, name='my_tickets'),

]
