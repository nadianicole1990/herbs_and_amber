# Generated by Django 4.2.15 on 2024-09-11 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_tincture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tincture',
            name='image',
            field=models.CharField(default='images/Default.JPG', max_length=100),
        ),
    ]
