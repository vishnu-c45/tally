# Generated by Django 4.0.4 on 2022-07-06 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tapp', '0008_create_units_conversion_create_units_first_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create_units',
            name='formal_name',
            field=models.CharField(blank=True, default='Null', max_length=225),
        ),
        migrations.AlterField(
            model_name='create_units',
            name='number_of_decimal_places',
            field=models.CharField(blank=True, default='Null', max_length=225),
        ),
        migrations.AlterField(
            model_name='create_units',
            name='symbol',
            field=models.CharField(blank=True, default='Null', max_length=225),
        ),
        migrations.AlterField(
            model_name='create_units',
            name='type',
            field=models.CharField(blank=True, default='Null', max_length=225),
        ),
    ]
