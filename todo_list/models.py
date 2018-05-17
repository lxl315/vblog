from django.db import models

# Create your models here.


class TodoList(models.Model):
    todo_id = models.AutoField(primary_key=True)
    todo_title =  models.CharField(max_length=100)
    todo_content = models.TextField()
    todo_finish_date = models.DateTimeField()
    finish_flag = models.CharField(max_length=2)


