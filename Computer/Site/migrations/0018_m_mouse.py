# Generated by Django 4.0.3 on 2022-03-21 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0017_delete_m_mouse'),
    ]

    operations = [
        migrations.CreateModel(
            name='M_Mouse',
            fields=[
                ('M_Mouse_id', models.IntegerField(help_text='ID компьютерной мыши', unique=True)),
                ('M_Mouse_name', models.CharField(help_text='Название компьютерной мыши', max_length=50, primary_key=True, serialize=False, verbose_name='Название компьютерной мыши')),
                ('M_Mouse_Image', models.ImageField(null=True, upload_to='')),
                ('M_Mouse_ConnectType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connecttype', verbose_name='Тип подключения')),
                ('M_Mouse_ConnectionInt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connectionint', verbose_name='Интерфейс подключения')),
                ('M_Mouse_DPI', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.m_mouse_dpi', verbose_name='Максимальное разрешение датчика')),
                ('M_Mouse_Frequency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.m_mouse_frequency', verbose_name='Частота обращения')),
                ('M_Mouse_Manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.manufacturer', verbose_name='Бренд')),
                ('M_Mouse_SenserModel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.m_mouse_sensermodel', verbose_name='Модель сенсора')),
            ],
        ),
    ]
