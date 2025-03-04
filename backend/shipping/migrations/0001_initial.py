# Generated by Django 5.1.6 on 2025-03-02 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_number', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('carrier', models.CharField(max_length=100)),
                ('estimated_delivery', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_transit', 'In Transit'), ('delivered', 'Delivered')], default='pending', max_length=20)),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping', to='transactions.transaction')),
            ],
        ),
    ]
