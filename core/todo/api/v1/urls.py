from django.urls import path
from todo.api.v1 import views
from rest_framework.routers import DefaultRouter


app_name = 'todo-api'

router = DefaultRouter()
router.register('task', views.TaskView, basename='task')

urlpatterns = router.urls

# urlpatterns = [
#     path('tasks/', views.TaskList.as_view({'get': 'list', 'post': 'create'}), name='task-list'),
#     path('task/<int:pk>/', views.TaskList.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update',
#                                                    'delete': 'destroy'}), name='task-detail'),
# ]
