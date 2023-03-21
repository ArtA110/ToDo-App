import django_filters.rest_framework as filters
from django.forms import DateTimeInput
from accounts.models import User


class UserFilter(filters.FilterSet):
    created_date_gt = filters.DateTimeFilter(field_name='created_date', lookup_expr='gt',
                                            widget=DateTimeInput(attrs={'type': 'datetime-local'}))
    created_date_lt = filters.DateTimeFilter(field_name='created_date', lookup_expr='lt',
                                             widget=DateTimeInput(attrs={'type': 'datetime-local'}))

    email = filters.ModelMultipleChoiceFilter(field_name='email', queryset=User.object.filter(is_active=True))

    class Meta:
        model = User
        fields = ['created_date_gt', 'created_date_lt', 'email']
