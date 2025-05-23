# Generated by Django 5.2.1 on 2025-05-13 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('date', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
                ('hour', models.CharField(max_length=100)),
                ('class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.class')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.teacher')),
            ],
        ),
    ]
