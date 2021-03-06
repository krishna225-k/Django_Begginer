# Generated by Django 3.0.2 on 2020-03-12 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('location', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
            ],
        ),
    ]
