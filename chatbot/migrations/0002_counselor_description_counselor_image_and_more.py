# Generated by Django 4.1.1 on 2022-09-23 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counselor',
            name='description',
            field=models.TextField(default='abc', verbose_name='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='counselor',
            name='image',
            field=models.TextField(default='abc', verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='counselor',
            name='user_name',
            field=models.CharField(default='abc', max_length=50, verbose_name='user_name'),
            preserve_default=False,
        ),
    ]
