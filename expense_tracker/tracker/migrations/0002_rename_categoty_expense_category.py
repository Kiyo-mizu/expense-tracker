# Generated by Django 5.1.4 on 2024-12-11 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='categoty',
            new_name='category',
        ),
    ]
