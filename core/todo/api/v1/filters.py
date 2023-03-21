import django_filters.rest_framework as filters
from todo.models import Task
from django.forms import CheckboxInput, DateTimeInput
from accounts.models import Profile


class TaskFilter(filters.FilterSet):
    created_date_gt = filters.DateTimeFilter(field_name='created_date', lookup_expr='gt',
                                            widget=DateTimeInput(attrs={'type': 'datetime-local'}))
    created_date_lt = filters.DateTimeFilter(field_name='created_date', lookup_expr='lt',
                                            widget=DateTimeInput(attrs={'type': 'datetime-local'}))
    updated_date_gt = filters.DateTimeFilter(field_name='updated_date', lookup_expr='gt',
                                            widget=DateTimeInput(attrs={'type': 'datetime-local'}))
    updated_date_lt = filters.DateTimeFilter(field_name='updated_date', lookup_expr='lt',
                                            widget=DateTimeInput(attrs={'type': 'datetime-local'}))
    isDone = filters.BooleanFilter(field_name='isDone', widget=CheckboxInput())
    user = filters.ModelMultipleChoiceFilter(field_name='user', queryset=Profile.objects.filter(user__is_active=True))

    class Meta:
        model = Task
        fields = ['created_date_gt', 'created_date_lt', 'updated_date_gt', 'updated_date_lt', 'isDone', 'user']
