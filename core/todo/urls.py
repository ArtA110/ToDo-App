from django.urls import path
from todo.views import createTask, updateTask, deleteTask, showTasks

app_name = 'todo'
urlpatterns = [
    path('create-task/', createTask, name='create_task'),
    path('update-task/<int:pk>/', updateTask, name='update_task'),
    path('delete-task/<int:pk>/', deleteTask, name='delete_task'),
    path('tasks/',showTasks, name='show_tasks'),
]
