# Generated by Django 3.2.8 on 2021-10-13 04:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('LSM', '0002_alter_obra_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
