# Generated by Django 3.0.2 on 2020-03-12 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=100)),
                ('sales', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('eid', models.AutoField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('sal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('student_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='multipleapp.Student')),
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='multipleapp.Customer')),
                ('emp_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='multipleapp.Emp')),
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('bname', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
            ],
            bases=('multipleapp.emp', 'multipleapp.customer', 'multipleapp.student'),
        ),
    ]
