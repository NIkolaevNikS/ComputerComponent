# Generated by Django 4.0.3 on 2022-05-19 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0053_alter_h_headset_h_headset_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='Manufacturer_image',
        ),
    ]