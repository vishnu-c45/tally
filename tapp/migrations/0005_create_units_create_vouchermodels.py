# Generated by Django 4.0.4 on 2022-06-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0004_create_stockgrp'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_units',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=225)),
                ('symbol', models.CharField(max_length=225)),
                ('formal_name', models.CharField(max_length=225)),
                ('number_of_decimal_places', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='create_VoucherModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('voucher_type', models.CharField(max_length=225)),
                ('abbreviation', models.CharField(max_length=225)),
                ('active_this_voucher_type', models.CharField(max_length=225)),
                ('method_voucher_numbering', models.CharField(max_length=225)),
                ('use_adv_conf', models.CharField(blank=True, max_length=225)),
                ('prvnt_duplictes', models.CharField(blank=True, default='Null', max_length=225)),
                ('use_effective_date', models.CharField(default='Null', max_length=225)),
                ('allow_zero_value_trns', models.CharField(max_length=225)),
                ('allow_naration_in_voucher', models.CharField(max_length=225)),
                ('make_optional', models.CharField(max_length=225)),
                ('provide_naration', models.CharField(max_length=225)),
                ('print_voucher', models.CharField(max_length=225)),
            ],
        ),
    ]
