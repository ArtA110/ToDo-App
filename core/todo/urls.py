from django.urls import path
from todo.views import createTask# , updateTask, deleteTask

app_name = 'todo'
urlpatterns = [
    path('create-task/', createTask, name='create_task'),
]
