# Generated by Django 4.2.15 on 2024-09-10 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Herb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('properties', models.TextField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='tincture',
            name='herbs',
        ),
        migrations.AddField(
            model_name='tincture',
            name='herbs',
            field=models.ManyToManyField(to='main_app.herb'),
        ),
    ]
