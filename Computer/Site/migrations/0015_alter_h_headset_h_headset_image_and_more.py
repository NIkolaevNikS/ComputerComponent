# Generated by Django 4.0.3 on 2022-03-20 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0014_h_headset_h_headset_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='h_headset',
            name='H_HeadSet_Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='k_keyboard',
            name='K_Keyboard_Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='m_mouse',
            name='M_Mouse_Image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='Manufacturer_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
