from django.db import models

# Create your models here

class ToDo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=False)
    edited_at = models.DateTimeField(blank=True)
    is_completed = models.BooleanField(default=False)

class ToDoItems(models.Model):
    todo_list = models.ForeignKey(ToDo, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(blank=False)
    edited_at = models.DateTimeField(blank=True)
    is_completed = models.BooleanField(default=False)
