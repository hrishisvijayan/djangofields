import email
from secrets import choice
from django.utils import timezone
from tkinter import CASCADE
from turtle import mode
from django.db import models
import datetime

# Create your models here.

print('now in models page')


class User(models.Model):
    name     = models.CharField(max_length=50)
    email    = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    image    = models.ImageField(null = True)
    video    = models.URLField(null=True)

class Data(models.Model):
    image = models.ImageField(upload_to='images')
    video = models.URLField()

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200,null=True)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

