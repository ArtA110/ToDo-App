from django.urls import path
from todo.api.v1 import views
app_name = 'todo-api'
urlpatterns = [
    path('tasks', views.TaskList.as_view({'get': 'list', 'post': 'create'}), name='task-list')
]
