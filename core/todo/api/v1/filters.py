import django_filters
from todo.models import Task


class TaskFilter(django_filters.FilterSet):
    created_date_gt = django_filters.DateTimeFilter(field_name='created_date', lookup_expr='gt')
    created_date_lt = django_filters.DateTimeFilter(field_name='created_date', lookup_expr='lt')
    updated_date_gt = django_filters.DateTimeFilter(field_name='updated_date', lookup_expr='gt')
    updated_date_lt = django_filters.DateTimeFilter(field_name='updated_date', lookup_expr='lt')

    class Meta:
        model = Task
        fields = ['created_date', 'updated_date', 'isDone']
