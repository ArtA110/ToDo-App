from django.urls import path
from .views import signup_view, complete_profile_view

app_name = 'accounts'
urlpatterns = [
    path('signup/', signup_view),
    path('complete-profile/', complete_profile_view),
]
