# Generated by Django 3.2.8 on 2021-10-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LSM', '0005_alter_obra_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obra',
            name='foto',
            field=models.SlugField(),
        ),
    ]
