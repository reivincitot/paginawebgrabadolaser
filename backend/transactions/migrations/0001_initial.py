# Generated by Django 4.2 on 2025-02-11 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True)),
                ('transaction_status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=100)),
                ('transaction_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('transaction_currency', models.CharField(blank=True, max_length=10, null=True)),
                ('transaction_method', models.CharField(blank=True, max_length=100, null=True)),
                ('transaction_response', models.TextField(blank=True, null=True)),
                ('payment_status', models.CharField(blank=True, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], max_length=20, null=True)),
                ('shipping_status', models.CharField(blank=True, choices=[('pending', 'Pending'), ('in_transit', 'In Transit'), ('delivered', 'Delivered')], max_length=20, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=20, null=True)),
                ('shipping_carrier', models.CharField(blank=True, max_length=100, null=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='orders.order')),
            ],
        ),
    ]
