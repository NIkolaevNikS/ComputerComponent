# Generated by Django 4.0.3 on 2022-03-21 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0024_rename_m_mouse_sensmodel_m_mouse_m_mouse_sensermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_mouse',
            name='M_Mouse_id',
            field=models.AutoField(help_text='ID компьютерной мыши', primary_key=True, serialize=False, unique=True),
        ),
    ]