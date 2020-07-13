from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
     path('todos', views.ToDoView.as_view(), name="todos"),
     path('todos/<int:pk>', views.ToDoDetailsView.as_view(), name="todo-details"),

     path('todos/<int:todo_pk>/todo-items', views.ToDoItemsView.as_view(), name="tod0-items" ),
     path('todos/<int:todo_pk>/todo-items/<int:pk>',views.ToDoItemsDetailsView.as_view(), name="todo-item-details"),
]
