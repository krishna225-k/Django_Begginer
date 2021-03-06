# Generated by Django 3.0.2 on 2020-02-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('school_name', models.CharField(max_length=50)),
                ('class_name', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('mobile', models.BigIntegerField()),
                ('telugu_marks', models.IntegerField()),
                ('hindi_marks', models.IntegerField()),
                ('english_marks', models.IntegerField()),
                ('maths_marks', models.IntegerField()),
                ('science_marks', models.IntegerField()),
                ('social_marks', models.IntegerField()),
            ],
        ),
    ]
