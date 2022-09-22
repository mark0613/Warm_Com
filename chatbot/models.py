from django.db import models
import datetime

class Counselor(models.Model):
    MALE = "男"
    FEMALE = "女"
    NONE = "不透露"
    GENDER_CHOICES = ((MALE, "男"), (FEMALE, "女"), (NONE, "不透露"))

    user_id = models.CharField('user_id', max_length=33)
    gender = models.CharField('gender', choices=GENDER_CHOICES, default=NONE, max_length=10)
    age = models.IntegerField('age', default=None, null=True, blank=True)
    job = models.CharField('job', max_length=255, null=True, blank=True)
    is_professional = models.BooleanField('is_professional', default=False)
    can_be_paired = models.BooleanField('can_be_paired', default=True)

class Target(models.Model):
    type = models.CharField('type', max_length=50)

class Article(models.Model):
    title = models.CharField('title', max_length=255)
    creator = models.CharField('creator', max_length=33)
    content = models.TextField('content')
    time = models.DateTimeField('time', default=datetime.date.today)

class Reply(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    creator = models.CharField('creator', max_length=33)
    content = models.TextField('content')
    time = models.DateTimeField('time', default=datetime.date.today)