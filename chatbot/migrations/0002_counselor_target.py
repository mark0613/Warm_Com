# Generated by Django 4.1.1 on 2022-09-22 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='counselor',
            name='target',
            field=models.ManyToManyField(blank=True, to='chatbot.target'),
        ),
    ]
