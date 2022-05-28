# Generated by Django 4.0.3 on 2022-03-19 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0007_connectionint_connecttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectionint',
            name='ConnectionInt_name',
            field=models.CharField(help_text='Интерфейс подключения', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='connecttype',
            name='ConnectType_name',
            field=models.CharField(help_text='Тип подключения', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='Manufacturer_name',
            field=models.CharField(help_text='Бренд', max_length=50, null=True),
        ),
    ]
