# Generated by Django 4.2 on 2025-02-11 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='img/products'),
        ),
    ]
