# Generated by Django 5.0.2 on 2024-02-10 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sydney_participants', models.IntegerField()),
                ('sydney_percentile', models.FloatField()),
                ('correct_answer_percentage_per_class', models.FloatField()),
                ('correct_answer', models.CharField(max_length=100)),
                ('participant', models.CharField(max_length=100)),
                ('student_score', models.FloatField()),
                ('category', models.CharField(max_length=100)),
                ('year_level_name', models.CharField(max_length=100)),
                ('correct_answer_id', models.IntegerField()),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_app.answers')),
                ('assessment_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_app.assessmentarea')),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_app.award')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_app.class')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_app.school')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_app.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_app.subject')),
            ],
        ),
    ]
