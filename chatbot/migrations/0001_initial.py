# Generated by Django 4.1.1 on 2022-09-22 07:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('creator', models.CharField(max_length=33, verbose_name='creator')),
                ('content', models.TextField(verbose_name='content')),
                ('time', models.DateTimeField(default=datetime.date.today, verbose_name='time')),
            ],
        ),
        migrations.CreateModel(
            name='Counselor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=33, verbose_name='user_id')),
                ('gender', models.CharField(choices=[('男', '男'), ('女', '女'), ('不透露', '不透露')], default='不透露', max_length=10, verbose_name='gender')),
                ('age', models.IntegerField(blank=True, default=None, null=True, verbose_name='age')),
                ('job', models.CharField(blank=True, max_length=255, null=True, verbose_name='job')),
                ('is_professional', models.BooleanField(default=False, verbose_name='is_professional')),
                ('can_be_paired', models.BooleanField(default=True, verbose_name='can_be_paired')),
            ],
        ),
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='type')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=33, verbose_name='creator')),
                ('content', models.TextField(verbose_name='content')),
                ('time', models.DateTimeField(default=datetime.date.today, verbose_name='time')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.article')),
            ],
        ),
    ]
