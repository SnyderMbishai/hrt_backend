import datetime
from django.db import models

# Create your models here

class ToDo(models.Model):
    title = models.CharField(max_length=128, blank=False)
    description = models.CharField(blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    edited_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

class ToDoItems(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)    
    todo = models.ForeignKey(ToDo, related_name="todo_items", on_delete=models.CASCADE)
