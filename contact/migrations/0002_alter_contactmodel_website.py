# Generated by Django 3.2.6 on 2021-08-11 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
