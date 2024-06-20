from django.contrib import admin
from .models import PassType, Subscription, User, Employee, Driver, Passenger

admin.site.register(PassType)
admin.site.register(Subscription)
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Driver)
admin.site.register(Passenger)
