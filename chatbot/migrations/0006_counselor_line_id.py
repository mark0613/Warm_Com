# Generated by Django 4.1.1 on 2022-09-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0005_merge_20220924_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='counselor',
            name='line_id',
            field=models.CharField(default='000', max_length=255, verbose_name='line_id'),
            preserve_default=False,
        ),
    ]