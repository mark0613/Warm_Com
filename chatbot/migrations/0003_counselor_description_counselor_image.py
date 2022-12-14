# Generated by Django 4.1.1 on 2022-09-22 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0002_counselor_target'),
    ]

    operations = [
        migrations.AddField(
            model_name='counselor',
            name='description',
            field=models.TextField(default='我是諮商師', verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='counselor',
            name='image',
            field=models.TextField(default='https://images.unsplash.com/photo-1481349518771-20055b2a7b24?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8cmFuZG9tfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60', verbose_name='image'),
            preserve_default=False,
        ),
    ]
