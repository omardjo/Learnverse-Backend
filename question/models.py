from django.db import models


class Question(models.Model):

    question = models.CharField(max_length=200)
    choices = models.CharField(max_length=200)
    solution = models.CharField(max_length=200)
   

    def __str__(self):
        return self.question
    
    class Meta:
        db_table ='questions'
