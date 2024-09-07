# Generated by Django 5.1 on 2024-08-30 08:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_info', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_info', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contract_date', models.DateField(auto_now_add=True)),
                ('delivery_date', models.DateField()),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending', max_length=50)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.buyer')),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.crop')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.farmer')),
            ],
        ),
    ]
