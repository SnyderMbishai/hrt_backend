from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, generics, viewsets

from .serializers import ToDoSerializer, ToDoItemsSerializer
from .models import ToDo, ToDoItems

class ToDoView(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

class ToDoDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

class ToDoItemsView(generics.ListCreateAPIView):
    serializer_class = ToDoItemsSerializer
    queryset = ToDoItems.objects.all()

class ToDoItemsDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoItemsSerializer
    queryset = ToDoItems.objects.all()
    