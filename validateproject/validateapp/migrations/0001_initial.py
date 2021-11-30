# Generated by Django 3.0.2 on 2020-03-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrationData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('password1', models.CharField(max_length=20)),
                ('password2', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]