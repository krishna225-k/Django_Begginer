# Generated by Django 3.0 on 2020-01-31 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='created_data',
            new_name='created_date',
        ),
    ]
