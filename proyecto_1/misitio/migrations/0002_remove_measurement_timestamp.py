# Generated by Django 5.1.4 on 2025-01-09 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('misitio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='timestamp',
        ),
    ]
