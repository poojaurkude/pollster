from django.db import models
from django.contrib.auth.models import User


class Question (models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publisher')

    def __str__(self):
        return self.question_text


class Choice (models.Model):
    # if qustion is deleted then automaticaly choices also deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Vote (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    vote= models.ForeignKey(User, on_delete=models.CASCADE)