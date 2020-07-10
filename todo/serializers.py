from rest_framework import serializers
from .models import ToDo, ToDoItems

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"

class ToDoItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItems
        fields = "__all__"