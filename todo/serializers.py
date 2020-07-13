from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import ToDo, ToDoItems

class ToDoItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItems
        fields = ("id","title","description", "created_at")
        read_only_fields = ("todo",)

    def create(self,validated_data):
        todo = get_object_or_404(ToDo, pk=self.context["view"].kwargs["todo_pk"])
        return ToDoItems.objects.create(**validated_data, todo=todo)

class ToDoSerializer(serializers.ModelSerializer):
    todo_items = ToDoItemsSerializer(many=True, read_only=True)
    class Meta:
        model = ToDo
        fields = ("title","description", "todo_items")
