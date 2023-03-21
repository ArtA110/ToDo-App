from django.urls import path, include
from .views import signup_view, complete_profile_view, login_view, logout_view
from accounts.api.v1 import urls

app_name = 'accounts'
urlpatterns = [
    path('api/v1/', include(urls)),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('complete-profile/', complete_profile_view),
]
