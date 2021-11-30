# Generated by Django 3.0 on 2020-01-31 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('mobile', models.BigIntegerField(null=True)),
                ('created_data', models.DateField(auto_now_add=True)),
            ],
        ),
    ]