# Generated by Django 3.0.3 on 2020-09-10 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='McqExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_topic', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('option_1', models.CharField(max_length=300)),
                ('option_2', models.CharField(max_length=300)),
                ('option_3', models.CharField(max_length=300)),
                ('option_4', models.CharField(max_length=300)),
                ('correct_ans', models.CharField(max_length=1)),
                ('mcq_exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mcq_exam', to='quiz.McqExam')),
            ],
        ),
    ]
