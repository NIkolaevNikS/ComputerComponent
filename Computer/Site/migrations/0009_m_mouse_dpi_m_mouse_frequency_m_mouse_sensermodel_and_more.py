# Generated by Django 4.0.3 on 2022-03-19 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0008_alter_connectionint_connectionint_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='M_Mouse_DPI',
            fields=[
                ('M_Mouse_DPI_id', models.AutoField(help_text='ID разрешение датчика', primary_key=True, serialize=False, unique=True)),
                ('M_Mouse_DPI_name', models.CharField(help_text='Максимальное разрешение датчика', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='M_Mouse_Frequency',
            fields=[
                ('M_Mouse_Frequency_id', models.AutoField(help_text='ID частоты', primary_key=True, serialize=False, unique=True)),
                ('M_Mouse_Frequency_name', models.CharField(help_text='Частота обновления', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='M_Mouse_SenserModel',
            fields=[
                ('M_Mouse_SenserModel_id', models.AutoField(help_text='ID модели сенсора', primary_key=True, serialize=False, unique=True)),
                ('M_Mouse_SenserModel_name', models.CharField(help_text='Модель сенсора', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='M_Mouse',
            fields=[
                ('M_Mouse_id', models.AutoField(help_text='ID интерфейса подключения', primary_key=True, serialize=False, unique=True)),
                ('M_Mouse_name', models.CharField(help_text='Интерфейс подключения', max_length=50, null=True)),
                ('M_Mouse_ConnectType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connecttype')),
                ('M_Mouse_ConnectionInt', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.connectionint')),
                ('M_Mouse_DPI', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.m_mouse_dpi')),
                ('M_Mouse_Frequency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.m_mouse_frequency')),
                ('M_Mouse_Manufacturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.manufacturer')),
                ('M_Mouse_SenserModel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Site.m_mouse_sensermodel')),
            ],
        ),
    ]