# Generated by Django 5.0.6 on 2024-06-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('single', 'Single Ticket'), ('return', 'Return Ticket')], max_length=10),
        ),
    ]
