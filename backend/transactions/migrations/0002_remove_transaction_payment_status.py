# Generated by Django 4.2 on 2025-02-11 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='payment_status',
        ),
    ]
