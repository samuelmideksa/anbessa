from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone


class User(AbstractUser):
    """Custom User Model"""

    phoneNumber = models.CharField(max_length=11)

    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

    def __str__(self):
        return self.username


class Passenger(User, models.Model):
    """Passenger Model"""

    # buyTicket
    # buySubscription(
    # makeComplaint(

    class Meta:
        verbose_name = 'Passenger'

    def __str__(self):
        return f'passenger {self.first_name} {self.last_name}'


class Employee(User, models.Model):
    """Employee Model"""
    role = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Employee'

    def __str__(self):
        return f'employee {self.id} {self.role}'


class Driver(Employee, models.Model):
    """Driver Model"""
    license = models.CharField(max_length=11)
    Employee.role = 'driver'

    class Meta:
        verbose_name = 'Driver'

    def __str__(self):
        return f'driver {self.id} {self.license}'


class PassType(models.Model):
    name = models.CharField(max_length=100)
    duration_days = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pass_type = models.ForeignKey(PassType, on_delete=models.CASCADE)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.end_date:
            self.end_date = self.start_date + timezone.timedelta(days=self.pass_type.duration_days)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.pass_type.name}"
