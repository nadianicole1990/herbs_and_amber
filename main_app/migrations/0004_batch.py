# Generated by Django 4.2.15 on 2024-09-10 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_herb_material_herb_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prep_date', models.DateField(verbose_name='prep date')),
                ('ready_date', models.DateField(verbose_name='ready date')),
                ('tincture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.tincture')),
            ],
        ),
    ]
